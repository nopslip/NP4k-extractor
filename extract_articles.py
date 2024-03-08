from newspaper import Article
import json
import logging
import time
import argparse

# Enable logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    args = parse_arguments()
    url_list = args.file
    output_format = args.output.lower() if args.output else 'kvp'  # Set default format to KVP
    unprocessed_urls = get_unprocessed_urls(url_list)
    if unprocessed_urls:
        logger.info(f'Found {len(unprocessed_urls)} URLs to process!')
        process_urls(unprocessed_urls, url_list, output_format)
    else:
        logger.info('Zero unprocessed URLs found...')

def get_unprocessed_urls(url_list):
    '''Read URLs from a local file specified in the config'''
    try:
        with open(url_list, 'r') as file:
            urls = [url.strip() for url in file.read().splitlines() if url.strip()]
            return urls
    except FileNotFoundError:
        logger.error(f'The file {url_list} was not found.')
        return []
    except Exception as e:
        logger.error(f'Error reading from {url_list}: {e}')
        return []

def process_urls(urls, url_list, output_format):
    '''Run newspaper4k against each URL and extract/produce metadata'''
    timestamp = int(time.time())
    output_filename = f'_output_{url_list}_{timestamp}.{"json" if output_format == "json" else "txt"}'
    articles_data = []

    for url in urls:
        if url:  # Check if URL is not empty
            logger.info(f'Processing URL: {url}')
            try:
                article_data = newspaper4k(url)
                articles_data.append(article_data)
            except Exception as e:
                logger.error(f'Error processing URL {url}: {e}')
                continue

    if output_format == 'json':
        write_json(articles_data, output_filename)
    else:  # Default to KVP
        write_kvp(articles_data, output_filename)

def write_json(articles_data, output_filename):
    try:
        with open(output_filename, 'w', encoding='utf-8') as f:
            json.dump(articles_data, f, ensure_ascii=False, indent=4)
        logger.info(f'Successfully wrote extracted data to {output_filename}')
    except Exception as e:
        logger.error(f'Error writing data to {output_filename}: {e}')

def write_kvp(articles_data, output_filename):
    try:
        with open(output_filename, 'w', encoding='utf-8') as f:
            for article in articles_data:
                for key, value in article.items():
                    if isinstance(value, list):
                        value = ', '.join(value)
                    if isinstance(value, str):
                        value = value.replace('\n', '\\n')
                    f.write(f"{key}: {value}\n")
                f.write("---\n")
            logger.info(f'Successfully wrote extracted data to {output_filename}')
    except Exception as e:
        logger.error(f'Error writing data to {output_filename}: {e}')

def newspaper4k(url):
    article = Article(url, fetch_images=False)
    processed_article = {
        "title": "",
        "keywords": [],
        "tags": [],
        "authors": [],
        "summary": "",
        "text": "",
        "publish_date": "",
        "url": "", 
    }
    try:
        article.download()
        article.parse()
        article.nlp()
        
        processed_article["title"] = article.title or "Not Found"
        processed_article["keywords"] = article.keywords if article.keywords is not None else []
        processed_article["tags"] = list(article.tags) if article.tags is not None else []
        processed_article["authors"] = article.authors if article.authors is not None else ["Not Found"]
        processed_article["summary"] = article.summary or "Not Found"
        processed_article["text"] = article.text or "Not Found"
        processed_article["publish_date"] = article.publish_date.isoformat() if article.publish_date else "Not Found"
        processed_article["url"] = url

    except Exception as e:
        logger.error(f'Failed to process article from {url}: {e}')
        raise e
    return processed_article

def parse_arguments():
    parser = argparse.ArgumentParser(description='Script to process URLs and extract information.')
    parser.add_argument('--file', type=str, required=True, help='The file containing the list of URLs to process.')
    parser.add_argument('--output', type=str, choices=['kvp', 'json'], help='The file format to write the extracted data in. Default is key value pairs. Options are [kvp, JSON]')
    # parser.add_argument('--verbose', action='store_true', help='Increase output verbosity')
    return parser.parse_args()

if __name__ == '__main__':
    main()
