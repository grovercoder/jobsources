# JobSources Analyzer

## Overview

JobSources Analyzer is a Python-based tool designed to intelligently extract job posting information from various online sources. It automates the process of identifying job detail page URLs and inferring the necessary CSS selectors to extract structured data such as job titles, descriptions, company names, and posting dates.

## Features

*   **Versatile URL Analysis:** Processes job listings from HTML pages, JSON feeds, and RSS feeds.
*   **Dynamic Selector Inference:** Utilizes Large Language Models (LLMs) to automatically determine CSS selectors for key job posting fields (title, description, company, etc.) from sample job detail pages.
*   **Intelligent Caching:** Implements a robust caching mechanism for downloaded content to optimize performance and reduce redundant network requests. Cached files are automatically cleaned up based on age.
*   **LLM Provider Agnostic:** Supports multiple LLM providers, including Google Gemini and Ollama, configurable via environment variables.
    *Note: The choice of LLM model can significantly impact the accuracy and quality of the extracted information. Experimentation with different models is encouraged to achieve optimal results.*

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-repo/jobsources.git
    cd jobsources
    ```

2.  **Install dependencies using `uv`:**
    ```bash
    uv init
    uv add selenium requests beautifulsoup4 feedparser python-dotenv google-generativeai
    ```
    *Note: `uv` is used for package management. If you don't have `uv` installed, please refer to its official documentation for installation instructions.*

3.  **Configure Environment Variables:**
    Create a `.env` file in the project root based on `example.env`.
    
    *   **`LLM_PROVIDER`**: Set to `gemini` or `ollama`.
    *   **`GEMINI_API_KEY`**: Your Google Gemini API key (required if `LLM_PROVIDER` is `gemini`).
    *   **`GEMINI_MODEL`**: (Optional) Specify the Gemini model to use (default: `gemini-pro`).
    *   **`OLLAMA_URL`**: (Optional) URL for your Ollama instance (default: `http://localhost:11434` if `LLM_PROVIDER` is `ollama`).
    *   **`OLLAMA_MODEL`**: (Optional) Ollama model to use (default: `llama2` if `LLM_PROVIDER` is `ollama`).
    *   **`CACHE_DIR`**: (Optional) Directory for caching downloaded content (default: `data/cache`).

    Example `.env` for Gemini:
    ```
    LLM_PROVIDER=gemini
    GEMINI_API_KEY=YOUR_GEMINI_API_KEY
    # CACHE_DIR=my_custom_cache
    ```

    Example `.env` for Ollama:
    ```
    LLM_PROVIDER=ollama
    OLLAMA_URL=http://localhost:11434
    OLLAMA_MODEL=llama2
    ```

## Usage

To analyze a URL, you can use the `Manager` class:

```python
import logging
from src.jobsources.analysis.manager import Manager

# Configure logging (optional)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Initialize the Manager
manager = Manager(logger=logger)

# URL to analyze (example)
url_to_analyze = "https://example.com/jobs"

# Analyze the URL
result = manager.analyze_url(url_to_analyze)

# Print the extracted information
import json
print(json.dumps(result, indent=2))
```

## Project Structure

*   `src/`: Contains the core Python source code.
    *   `jobsources/analysis/manager.py`: The main logic for URL analysis and selector inference.
*   `docs/`: Project documentation, including detailed requirements.
*   `data/cache/`: Default directory for cached web content.
*   `scripts/`: Utility scripts (e.g., for linting).

## Development Standards

Refer to `GEMINI.md` for detailed development guidelines, including code standards, testing procedures, and revision control practices.
