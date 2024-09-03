from flask import Flask, jsonify, request
from dotenv import load_dotenv
import os
from firecrawl import FirecrawlApp
import requests
import json

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Initialize FirecrawlApp with the API key
firecrawl_api_key = os.getenv('FIRECRAWL_API_KEY')
firecrawl_app = FirecrawlApp(api_key=firecrawl_api_key)

# Azure Translator configuration
translator_endpoint = os.getenv('TRANSLATOR_ENDPOINT')
translator_key = os.getenv('TRANSLATOR_KEY')
translator_region = os.getenv('TRANSLATOR_REGION')

def translate_text(text, to_language='es'):  # Change the language code to 'es' for Spanish
    translate_url = f"{translator_endpoint}/translate"
    headers = {
        'Ocp-Apim-Subscription-Key': translator_key,
        'Ocp-Apim-Subscription-Region': translator_region,
        'Content-Type': 'application/json'
    }
    body = [{'text': text}]
    params = {
        'api-version': '3.0',
        'to': to_language
    }
    response = requests.post(translate_url, headers=headers, params=params, json=body)
    response.raise_for_status()
    translation_result = response.json()
    return translation_result[0]['translations'][0]['text']

def decode_unicode(text):
    return text.encode('utf-8').decode('unicode_escape')

@app.route('/')
def home():
    return 'Welcome to the Flask app!'

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    url = data.get('url')
    action = data.get('action')
    
    if not url or not action:
        return jsonify({'error': 'URL and action are required parameters'}), 400

    try:
        if action == 'scrape':
            scrape_result = firecrawl_app.scrape_url(url, params={'formats': ['markdown']})
            print("Scrape result:", scrape_result)
            if 'markdown' in scrape_result:
                markdown_content = scrape_result['markdown']
            else:
                return jsonify({'error': 'Scrape result does not contain "markdown"'}), 500

        elif action == 'crawl':
            crawl_status = firecrawl_app.crawl_url(
                url, 
                params={
                    'limit': 100, 
                    'scrapeOptions': {'formats': ['markdown']}
                }
            )
            print("Crawl status:", crawl_status)
            if 'markdown' in crawl_status:
                markdown_content = crawl_status['markdown']
            else:
                return jsonify({'error': 'Crawl result does not contain "markdown"'}), 500

        else:
            return jsonify({'error': 'Invalid action. Use "scrape" or "crawl"'}), 400

        # Decode any Unicode escape sequences in the markdown content
        markdown_content = decode_unicode(markdown_content)

        # Translate the markdown content to Spanish
        translated_text = translate_text(markdown_content)

        # Decode any Unicode escape sequences in the translated text
        translated_text = decode_unicode(translated_text)

        return jsonify({'status': 'success', 'translated_data': translated_text})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
