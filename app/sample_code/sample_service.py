from app.sample_code import sample_core
from app.utils.text_utils import *

import logging
logger = logging.getLogger(__name__)


def sample_services(response_object):
    """ Function to """
    urls = response_object.get("urls", [])
    sample_response = sample_core.parallel_crawl(urls)

    response_data = create_response_object(len(sample_response), sample_response, STATUS_SUCCESS)
    return response_data


def create_response_object(len_data, data, message):
    """ Function to """
    if len_data != 0:
        response = {'status': "OK", 'message': message,
                    'result': data}
        logger.info(message)
        return response
    else:
        response = {'status': "Failed", 'message': message,
                    'result': data}
        return response
