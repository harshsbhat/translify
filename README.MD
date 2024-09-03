
# Web Content Translation API

## Overview

This API allows you to effortlessly convert web content into Spanish. Whether you want to scrape or crawl a webpage, simply input the URL, choose your action, and the API will handle the translation for you. It's designed to be quick, accurate, and easy to use—perfect for developers needing seamless content localization.

## Features

- **Scrape or Crawl**: Choose between scraping a single page or crawling multiple pages.
- **Language Translation**: Automatically translates the content into Spanish.
- **User-Friendly**: Simple and efficient for fast integration into your projects.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/harshsbhat/translify.git
    cd translify/backend
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the `backend` directory and add your environment variables:
    ```
    FIRECRAWL_API_KEY=your_firecrawl_api_key
    TRANSLATOR_ENDPOINT=your_azure_translator_endpoint
    TRANSLATOR_KEY=your_azure_translator_key
    TRANSLATOR_REGION=your_azure_translator_region
    ```

## Usage
VIDEO EXAMPLE OF USAGE:
https://www.loom.com/share/842f3de485784a9ca8eaefb711d7e02f?sid=52d0f8d1-fe1c-4c0b-84f7-87642116a49b

1. Start the Flask application:
    ```bash
    python app.py
    ```

2. Make a POST request to `/translate` with the following JSON payload:
    ```json
    {
        "url": "https://example.com",
        "action": "scrape"  // or "crawl"
    }
    ```

3. The API will return the translated content in Spanish.

## Example Request

```bash
curl -X POST http://localhost:5000/translate \
-H "Content-Type: application/json" \
-d '{
    "url": "https://example.com",
    "action": "scrape"
}'
