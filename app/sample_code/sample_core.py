from configuration import num_url
import logging
from newsplease import NewsPlease

logger = logging.getLogger(__name__)


def get_url_batches(urls):
    batches = [urls[i:i + num_url] for i in range(0, len(urls), num_url)]
    return batches

def get_dict(crawlled_data):
    return data_crawled=[{i: j.get_dict()} for obj in crawlled_data for i, j in obj.items()]

def parallel_crawl(urls):
    url_batches = get_url_batches(urls)

    crawlled_data = []

    for batch in url_batches:
        data = NewsPlease.from_urls(batch)
        crawlled_data.append(data)

    data_crawled = get_dict(crawlled_data)
    logger.info(f"get response {data_crawled}")

    return data_crawled

