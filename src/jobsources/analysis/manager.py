"""Module for managing job source analysis and data extraction."""

import logging
import os
import json
import hashlib
from datetime import datetime, timedelta
from urllib.parse import urljoin

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
import google.generativeai as genai
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import feedparser


class NoOpLogger:
    """A logger that does nothing."""
    def debug(self, msg, *args, **kwargs):
        """No-op debug method."""
    def info(self, msg, *args, **kwargs):
        """No-op info method."""
    def warning(self, msg, *args, **kwargs):
        """No-op warning method."""
    def error(self, msg, *args, **kwargs):
        """No-op error method."""
    def critical(self, msg, *args, **kwargs):
        """No-op critical method."""
    def isEnabledFor(self, level): # pylint: disable=invalid-name, unused-argument
        """No-op isEnabledFor method."""
        return False


class Manager: # pylint: disable=too-many-instance-attributes
    """Manages the analysis of job source URLs and extraction of job posting data."""
    def __init__(self, logger=None):
        self.logger = logger if logger is not None else logging.getLogger(__name__)
        load_dotenv() # Load environment variables from .env file

        self.llm_provider = os.getenv("LLM_PROVIDER", "gemini").lower()
        self.model = None # Initialize model to None

        if self.llm_provider == "gemini":
            gemini_api_key = os.getenv("GEMINI_API_KEY")
            if not gemini_api_key:
                raise ValueError("GEMINI_API_KEY not found in .env file.")

            gemini_model_name = os.getenv("GEMINI_MODEL", "gemini-pro")
            genai.configure(api_key=gemini_api_key)
            self.model = genai.GenerativeModel(gemini_model_name)
            self.logger.info("Using Gemini LLM: %s", gemini_model_name)
        elif self.llm_provider == "ollama":
            self.ollama_url = os.getenv("OLLAMA_URL", "http://localhost:11434")
            self.ollama_model = os.getenv("OLLAMA_MODEL", "llama2")
            self.logger.info(
                "Using Ollama LLM: %s at %s",
                self.ollama_model,
                self.ollama_url
            )
            # No direct model object for Ollama, will use requests directly
        else:
            raise ValueError(f"Unsupported LLM_PROVIDER: {self.llm_provider}. Must be 'gemini' or 'ollama'.")

        # Setup Chrome options for headless browsing
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        try:
            self.driver = webdriver.Chrome(options=chrome_options)
        except WebDriverException as e:
            self.logger.error("Error initializing WebDriver: %s", e)
            self.driver = None

        # Determine cache directory and create if it doesn't exist
        self.cache_dir_name = os.getenv("CACHE_DIR", "data/cache")
        self.data_dir = os.path.join(os.getcwd(), self.cache_dir_name)
        os.makedirs(self.data_dir, exist_ok=True)

        # Clean up old cache files on startup
        self._clean_old_cache_files()

    def _clean_old_cache_files(self):
        """
        Deletes files in the cache directory older than 12 hours.
        """
        self.logger.info("Cleaning cache directory: %s", self.data_dir)
        now = datetime.now()
        for filename in os.listdir(self.data_dir):
            file_path = os.path.join(self.data_dir, filename)
            if os.path.isfile(file_path):
                file_mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))
                if now - file_mod_time > timedelta(hours=12):
                    try:
                        os.remove(file_path)
                        self.logger.info("Removed old cache file: %s", filename)
                    except OSError as e:
                        self.logger.error("Error removing file %s: %s", filename, e)

    def __del__(self):
        # Ensure the browser is closed when the Manager object is destroyed
        if hasattr(self, 'driver') and self.driver:
            self.driver.quit()

    # pylint: disable=no-else-return
    def _generate_content_with_llm(self, prompt: str) -> str:
        """
        Generates content using the configured LLM (Gemini or Ollama).
        """
        if self.llm_provider == "gemini":
            response = self.model.generate_content(prompt)
            return response.text
        elif self.llm_provider == "ollama":
            headers = {"Content-Type": "application/json"}
            data = {
                "model": self.ollama_model,
                "messages": [
                    {
                        "role": "system",
                        "content": (
                            "You are a strict JSON generator. "
                            "Always respond with ONLY valid JSON. "
                            "Do not include explanations, markdown, or commentary."
                        ),
                    },
                    {
                        "role": "user",
                        "content": prompt,
                    },
                ],
                "stream": False, # We want the full response at once
                # "stop": ["```", "\n\n", "</xml>", "###", "END", "}"]
            }
            try:
                response = requests.post(
                    f"{self.ollama_url}/api/generate",
                    headers=headers,
                    json=data,
                    timeout=10
                )
                response.raise_for_status()
                ollama_response_json = response.json()
                return ollama_response_json.get("response", "") # Use .get for safety
            except requests.exceptions.RequestException as e:
                self.logger.error("Error communicating with Ollama: %s", e)
                return ""
        else: # Changed from elif
            raise ValueError(f"Unsupported LLM_PROVIDER: {self.llm_provider}")

    def _get_url_content(self, url: str) -> tuple[str, str]: # pylint: disable=too-many-branches, too-many-statements
        """
        Gets the content of a URL, either from cache or by downloading it.
        Returns a tuple of (file_path, map_type).
        """
        self.logger.info("Getting content for URL: %s", url)

        # Create a unique filename for the URL
        url_hash = hashlib.md5(url.encode('utf-8')).hexdigest()
        cached_file_base = os.path.join(self.data_dir, url_hash)

        map_type = "html" # Default to HTML, will be refined
        file_path = ""

        # Check for cached file with any known extension
        for ext in ["html", "json", "xml"]:
            potential_cached_file = f"{cached_file_base}.{ext}"
            if os.path.exists(potential_cached_file):
                file_mod_time = datetime.fromtimestamp(os.path.getmtime(potential_cached_file))
                if datetime.now() - file_mod_time < timedelta(hours=6):
                    self.logger.info("Using cached file: %s", potential_cached_file)
                    return potential_cached_file, ext # Return the actual extension as map_type

        # If not cached or too old, download
        try:
            # Infer type from URL extension or path segment (initial guess)
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            content = response.text

            # Determine map_type based on Content-Type header
            content_type_header = response.headers.get('Content-Type', '').lower()
            if 'application/json' in content_type_header:
                map_type = "json"
            elif 'application/xml' in content_type_header or 'text/xml' in content_type_header or 'application/rss+xml' in content_type_header:
                map_type = "rss"
            else:
                map_type = "html"

            file_path = f"{cached_file_base}.{map_type}"

            if map_type == "html":
                if self.driver:
                    try:
                        self.driver.get(url)
                        content = self.driver.page_source
                    except WebDriverException as e:
                        self.logger.warning(
                            "Selenium failed to get page source; falling back to requests content: %s", e
                        )
                else:
                    self.logger.info("WebDriver not initialized. Using requests content for HTML.")

            # Fallback to content-based detection if MIME type is not specific or for initial requests content
            if map_type == "html": # Only try to infer if it's still HTML
                try:
                    json.loads(content)
                    map_type = "json"
                    file_path = f"{cached_file_base}.json"
                except json.JSONDecodeError:
                    try:
                        BeautifulSoup(content, 'xml')
                        map_type = "rss"
                        file_path = f"{cached_file_base}.xml"
                    except (json.JSONDecodeError, Exception):
                        pass # Keep as HTML if neither JSON nor XML

            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            self.logger.info("Downloaded and cached content to: %s with type: %s", file_path, map_type)
            return file_path, map_type

        except requests.exceptions.RequestException as e:
            self.logger.error("Download error (requests): %s", e)
            return "", ""
        except WebDriverException as e:
            self.logger.error("Selenium download failed: %s", e)
            return "", ""
        except IOError as e:
            self.logger.error("Error writing to file: %s", e)
            return "", ""
        except Exception as e:
            self.logger.error("An unexpected error occurred during download: %s", e)
            return "", ""



    # pylint: disable=too-many-branches, too-many-nested-blocks
    def _extract_postings(self, content: str, map_type: str, postings_url_selector: str, postings_title_selector: str) -> list:
        """
        Extracts job postings (URLs and titles) from listing content based on map_type and selectors.
        """
        self.logger.debug(
            "Extracting postings (URL: %s, Title: %s)",
            postings_url_selector,
            postings_title_selector)
        postings = []
        if not postings_url_selector or not postings_title_selector:
            self.logger.debug(
                "Missing selectors (URL: %s, Title: %s)",
                postings_url_selector,
                postings_title_selector)
            return []

        if map_type == "html":
            soup = BeautifulSoup(content, 'html.parser')
            url_elements = soup.select(postings_url_selector)
            title_elements = soup.select(postings_title_selector)

            # Assuming a 1:1 correspondence and same order for simplicity
            for i in range(min(len(url_elements), len(title_elements))):
                url = url_elements[i].get('href')
                title = title_elements[i].get_text(strip=True)
                if url and title:
                    postings.append({"url": url, "title": title})
        elif map_type == "json":
            try:
                data = json.loads(content)
                # This is a simplified approach. A more robust solution would involve
                # a JSON path parser or more sophisticated LLM output for JSON structures.
                # For now, assuming direct keys or simple array access.
                # The LLM should provide paths like 'jobs[0].url' or 'items.url'
                # This part needs careful consideration based on actual JSON structures.
                # For demonstration, let's assume the LLM gives a path like 'jobs.url'
                # and 'jobs.title' and we need to iterate over 'jobs'.

                # Simple example: if postings_url_selector is 'url' and content is a list of dicts
                if isinstance(data, list):
                    for item in data:
                        url = item.get(postings_url_selector)
                        title = item.get(postings_title_selector)
                        if url and title:
                            postings.append({"url": url, "title": title})
                elif isinstance(data, dict):
                    # Attempt to find a list within the dict
                    # This is highly dependent on the JSON structure
                    for _, value in data.items():
                        if isinstance(value, list):
                            for item in value:
                                url = item.get(postings_url_selector)
                                title = item.get(postings_title_selector)
                                if url and title:
                                    postings.append({"url": url, "title": title})

            except json.JSONDecodeError:
                self.logger.error("Invalid JSON content.")
        elif map_type == "rss":
            feed = feedparser.parse(content)
            for entry in feed.entries:
                url = entry.link
                title = entry.title
                if url and title:
                    postings.append({"url": url, "title": title})
        self.logger.debug("Found %d postings.", len(postings))
        return postings

    def _analyze_listing_with_gemini(self, content: str, content_type: str, mapping_object_template: dict) -> dict: # pylint: disable=too-many-locals
        """
        Analyzes the given listing content using Gemini LLM to extract mapping information.
        """
        self.logger.info("Analyzing listing content with %s LLM (type: %s)...", self.llm_provider.capitalize(), content_type)
        self.logger.info("")

        base_prompt = """
        You are a parser. Output JSON only. No explanations.
        If you cannot find a value, return an empty string.

        REQUIRED OUTPUT FORMAT:
        ```json
        {
          "source_name": "",
          "postings_url_selector": "",
          "postings_title_selector": ""
        }
        ```

        EXAMPLE OUTPUT:
        ```json
        {
          "source_name": "Example Job Board",
          "postings_url_selector": "a.job-link",
          "postings_title_selector": ".job-title"
        }
        ```

        Analyze the provided content to infer the `source_name`, `postings_url_selector`, and `postings_title_selector`.

        The values for `postings_url_selector` and `postings_title_selector` depend on the content type:
        - For HTML content, provide CSS selectors.
        - For JSON content, provide JSON paths (e.g., `jobs[0].url` or `url`).
        - For RSS/XML content, provide XPath expressions (e.g., `//item/link` or `//item/title`).

        If a field is not found or not applicable, use an empty string for its value.
        """

        if content_type == "html":
            specific_prompt = f"""
            The content provided is HTML from a job listing page.
            Infer CSS selectors for all fields. For `job_postings.*` fields, assume the selectors would apply to a typical job detail page linked from this listing.

            HTML Content:
            ```html
            {content}
            ```
            """
        elif content_type == "json":
            specific_prompt = f"""
            The content provided is a JSON string representing a job feed.
            Infer JSON keys/paths for `job_sources.*` fields. For `job_postings.*` fields, infer CSS selectors, assuming the job detail page (linked via `job_sources.post_urls`) is HTML.

            JSON Content:
            ```json
            {content}
            ```
            """
        elif content_type == "rss":
            specific_prompt = f"""
            The content provided is an RSS/XML string representing a job feed.
            Infer XPath expressions for `job_sources.*` fields. For `job_postings.*` fields, infer CSS selectors, assuming the job detail page (linked via `job_sources.post_urls`) is HTML.
            Also, extract a `sample_detail_url` from one of the job listing items (e.g., from a <link> tag within an <item>).

            RSS/XML Content:
            ```xml
            {content}
            ```
            """
        else:
            raise ValueError(f"Unsupported content type: {content_type}")

        prompt = base_prompt + specific_prompt

        # For debugging: Write the prompt to a file
        if self.logger.isEnabledFor(logging.DEBUG):
            debug_prompt_file_path = os.path.join(self.data_dir, "prompt_listing.md")
            with open(debug_prompt_file_path, 'w', encoding='utf-8') as f:
                f.write(prompt)
            self.logger.debug("Prompt written to: %s", debug_prompt_file_path)

        try:
            raw_llm_response = self._generate_content_with_llm(prompt)
            self.logger.debug("Raw LLM response: %s", raw_llm_response)

            json_string = ""
            # Attempt to find the first and last curly braces to extract the JSON string
            start_index = raw_llm_response.find('{')
            end_index = raw_llm_response.rfind('}')

            if start_index != -1 and end_index != -1 and end_index > start_index:
                json_string = raw_llm_response[start_index : end_index + 1]
            else:
                # Fallback to stripping markdown if braces not found or invalid range
                if raw_llm_response.startswith("```json") and raw_llm_response.endswith("```"):
                    json_string = raw_llm_response[len("```json"):-len("```")].strip()
                else:
                    json_string = raw_llm_response.strip()

            extracted_data = json.loads(json_string)

            # Update mapping_object_template with extracted data
            mapping_object_template["source_name"] = \
                extracted_data.get("source_name", "")
            mapping_object_template["selectors"]["postings_url_selector"] = \
                extracted_data.get("postings_url_selector", "")
            mapping_object_template["selectors"]["postings_title_selector"] = \
                extracted_data.get("postings_title_selector", "")

            return extracted_data

        except json.JSONDecodeError as e:
            self.logger.error("Error decoding JSON from LLM response: %s", e)
            self.logger.error("Problematic JSON string: %s", json_string)
            return mapping_object_template
        except Exception as e: # Catch any other unexpected errors # pylint: disable=broad-exception-caught
            self.logger.error("Error analyzing content with Gemini LLM: %s", e)
            return mapping_object_template

    def _analyze_detail_with_gemini(self, content: str, content_type: str, mapping_object_template: dict) -> dict:
        """
        Analyzes the given detail content using Gemini LLM to extract mapping information.
        """
        self.logger.info("Analyzing detail content with %s LLM (type: %s)...", self.llm_provider.capitalize(), content_type)

        base_prompt = """
        You are a parser. Output JSON only. No explanations.
        If you cannot find a value, return an empty string.

        REQUIRED OUTPUT FORMAT:
        ```json
        {
          "selectors": {
            "title": "",
            "description": "",
            "company": "",
            "company_url": "",
            "posted_date": ""
          }
        }
        ```

        EXAMPLE OUTPUT:
        ```json
        {
          "selectors": {
            "title": "h1.job-title",
            "description": "div.job-description",
            "company": ".company-name",
            "company_url": "a.company-name",
            "posted_date": ".posted-date"
          }
        }
        ```

        Analyze the provided HTML content from a job detail page and infer the CSS selectors for the following fields:
        - `title`: The job title or position name.
        - `description`: The full job description content.
        - `company`: The company name.
        - `company_url`: The URL of the company.
        - `posted_date`: The date the job was posted.

        If a field is not found or not applicable, use an empty string for its value.
        """

        if content_type == "html":
            specific_prompt = f"""
            The content provided is HTML from a job detail page. Carefully analyze this HTML content.
            Infer the most accurate CSS selectors for the following job detail fields:
            - `title`: The job title or position name.
            - `description`: The full job description content.
            - `company`: The company name.
            - `company_url`: The URL of the company.
            - `posted_date`: The date the job was posted.

            HTML Content:
            ```html
            {content}
            ```
            """
        else:
            raise ValueError(f"Unsupported content type for detail analysis: {content_type}")

        prompt = base_prompt + specific_prompt

        # For debugging: Write the prompt to a file
        debug_prompt_file_path = os.path.join(self.data_dir, "prompt_detail.md")
        if self.logger.isEnabledFor(logging.DEBUG):
            with open(debug_prompt_file_path, 'w', encoding='utf-8') as f:
                f.write(prompt)
            self.logger.debug("Prompt written to: %s", debug_prompt_file_path)

        try:
            raw_llm_response = self._generate_content_with_llm(prompt)
            self.logger.debug("Raw LLM response: %s", raw_llm_response)

            json_string = ""
            # Attempt to find the first and last curly braces to extract the JSON string
            start_index = raw_llm_response.find('{')
            end_index = raw_llm_response.rfind('}')

            if start_index != -1 and end_index != -1 and end_index > start_index:
                json_string = raw_llm_response[start_index : end_index + 1]
            else:
                # Fallback to stripping markdown if braces not found or invalid range
                if raw_llm_response.startswith("```json") and raw_llm_response.endswith("```"):
                    json_string = raw_llm_response[len("```json"):-len("```")].strip()
                else:
                    json_string = raw_llm_response.strip()

            extracted_data = json.loads(json_string)

            mapping_object_template["selectors"].update(extracted_data.get("selectors", {}))

            return extracted_data

        except json.JSONDecodeError as e:
            self.logger.error("Error decoding JSON from LLM response: %s", e)
            self.logger.error("Problematic JSON string: %s", json_string)
            return mapping_object_template
        except Exception as e: # Catch any other unexpected errors # pylint: disable=broad-exception-caught
            self.logger.error("Error analyzing content with Gemini LLM: %s", e)
            return mapping_object_template

    # pylint: disable=no-else-return
    def _analyze_with_gemini(self, content: str, content_type: str, analysis_type: str, mapping_object_template: dict) -> dict:
        """
        Dispatches to the appropriate Gemini LLM analysis method based on analysis_type.
        """
        if analysis_type == "listing":
            return self._analyze_listing_with_gemini(content, content_type, mapping_object_template)
        elif analysis_type == "detail":
            return self._analyze_detail_with_gemini(content, content_type, mapping_object_template)
        else:
            raise ValueError(f"Unknown analysis_type: {analysis_type}")

    def analyze_url(self, url: str, logger=None) -> dict:
        """Analyzes the given URL and returns the mapping object."""
        self.logger = logger if logger is not None else NoOpLogger()
        mapping_object = {
            "source_name": "",
            "selectors": {
                "title": "",
                "description": "",
                "company": "",
                "company_url": "",
                "posted_date": "",
                "postings_url_selector": "",
                "postings_title_selector": ""
            },
            "postings": []
        }

        try:
            listing_file_path, map_type = self._get_url_content(url)
            if not listing_file_path:
                self.logger.error("Failed to download listing URL.")
                return mapping_object

            with open(listing_file_path, 'r', encoding='utf-8') as f:
                listing_content = f.read()

            # Analyze listing with Gemini to get source_name and posting selectors
            llm_listing_data = self._analyze_with_gemini(listing_content, map_type, "listing", mapping_object)

            mapping_object["source_name"] = llm_listing_data.get("source_name", "")
            mapping_object["selectors"]["postings_url_selector"] = llm_listing_data.get("postings_url_selector", "")
            mapping_object["selectors"]["postings_title_selector"] = llm_listing_data.get("postings_title_selector", "")

            # Extract postings from the listing content
            self.logger.debug("DEBUG: Selectors before _extract_postings: %s", mapping_object['selectors'])
            mapping_object["postings"] = self._extract_postings(listing_content, map_type,
                                                               mapping_object["selectors"].get("postings_url_selector"),
                                                               mapping_object["selectors"].get("postings_title_selector"))

            # If postings are found, select a sample and analyze the detail page
            if mapping_object["postings"]:
                sample_detail_url = urljoin(url, mapping_object["postings"][0]["url"]) # Take the first posting as sample and make it absolute
                self.logger.info("Analyzing sample detail URL: %s", sample_detail_url)

                detail_file_path, detail_map_type = self._get_url_content(sample_detail_url)
                if not detail_file_path:
                    self.logger.error("Failed to download sample detail URL: %s", sample_detail_url)
                    return mapping_object

                with open(detail_file_path, 'r', encoding='utf-8') as f:
                    detail_content = f.read()

                # Analyze detail page with Gemini to get detail selectors
                llm_detail_data = self._analyze_with_gemini(detail_content, detail_map_type, "detail", mapping_object)
                mapping_object["selectors"].update(llm_detail_data.get("selectors", {}))
            else:
                self.logger.info("No postings found to extract a sample detail URL.")

        except requests.exceptions.RequestException as e:
            self.logger.error("An error occurred during network request: %s", e)
        except IOError as e:
            self.logger.error("An error occurred during file operation: %s", e)
        except Exception as e:
            self.logger.error("An unexpected error occurred during URL analysis: %s", e)
        finally:
            # No temporary files to clean up as _get_url_content handles caching
            pass

        return mapping_object
