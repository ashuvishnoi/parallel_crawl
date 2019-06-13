from newsplease import NewsPlease
import numpy as np

from configuration import num_url

import logging
logger = logging.getLogger(__name__)


def parallel_crawl(urls):

    url = np.array(urls)
    i = 0

    crawlled_data = []

    while i < url.shape[0]:
        if i + num_url < url.shape[0]:
            slice = url[i:i + num_url]
            i = i + num_url
            data = NewsPlease.from_urls(slice)
            crawlled_data.append(data)

        else:
            slice = url[i:url.shape[0]]
            data = NewsPlease.from_urls(slice)
            crawlled_data.append(data)

            break

    logger.info("Returned the crawlled data")

    return crawlled_data
