# Project Requirements

The goal of this project is to analyze a given URL to:
1. Extract a list of URLs to job detail pages.
2. Provide CSS selectors to find specific data fields on those job detail pages.

The incoming URL may point to an HTML page with a job listing, or it may be a feed page (JSON or RSS based). The listing page itself is primarily a gateway to identify and extract the URLs of individual job postings. A sample URL from the extracted list of job postings will then be used to determine the necessary CSS selectors for data extraction from the job detail page.

## Return Object Structure

The expected return object will be similar to this sample:
```json
{
  "source_name": "name of job source",
  "selectors": {
    "title": "#job-title",
    "description": ".job-description",
    "company": ".company-name",
    "company_url": "a.company-name",
    "posted_date": ".published-date"
  },
  "postings": []
}
```

## Data Handling and Storage

When downloading a URL for analysis, the content should be stored in a configurable cache directory. This directory can be specified via the `CACHE_DIR` environment variable, and defaults to `data/cache` if not set. To optimize performance and reduce redundant downloads:
- Any cached files older than 12 hours will be automatically deleted when the process starts.
- If a request is made for a URL that has already been downloaded, the existing file in the cache directory should be used if it is less than 6 hours old.
- If no such file is found, or if the existing file is older than 6 hours, the URL content should be downloaded again.

## Feed Processing

For RSS feeds, it is crucial to utilize a dedicated library like `feedparser` for robust and efficient parsing, rather than attempting to build a custom interpreter. This ensures proper handling of various RSS formats and reduces development overhead.

## CSS Selector Extraction

The process involves:
1. Interpreting the initial URL (HTML page or feed) to identify and extract a list of job posting detail URLs.
2. Selecting a sample job detail URL from this list.
3. Analyzing the content of the sample job detail page to determine the appropriate CSS selectors for fields such as `title`, `description`, `company`, `company_url`, and `posted_date`.