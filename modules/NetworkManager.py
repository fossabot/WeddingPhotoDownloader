# -*- coding: utf-8 -*-
""" Module in charge of network requests """
try:
    import requests
    import sys
    from resources.configuration import WEEDING_WEBSITE_BASE_URL, REQUESTS_HEADERS
    from src.logger import logger
except ModuleNotFoundError:
    print("Something went wrong while importing dependencies. Please, check the requirements file")
    sys.exit(1)


def check_gallery_availability(code: str) -> bool:
    """
    Check if the gallery corresponding to the received code exists or is available

    :param str code: The code of the gallery to download
    :return: True if the website pointed to by the URL exists or is available, False otherwise
    :rtype: bool
    """

    gallery_url = "".join([WEEDING_WEBSITE_BASE_URL, code])
    try:
        response = requests.get(gallery_url, headers=REQUESTS_HEADERS)
        if response.status_code == requests.codes['ok']:
            return True
    except requests.exceptions.HTTPError as http_error:
        http_error_line = "Http Error: {} \nURL: {}".format(http_error, gallery_url)
        logger.error(http_error_line)
        print(http_error_line)
    except requests.exceptions.ConnectionError as connection_error:
        connection_error_line = "Error Connecting: {} \nURL: {}".format(connection_error, gallery_url)
        logger.error(connection_error_line)
        print(connection_error_line)
    except requests.exceptions.Timeout as timeout_error:
        timeout_error_line = "Timeout Error: {} \nURL: {}".format(timeout_error, gallery_url)
        logger.error(timeout_error_line)
        print(timeout_error_line)
    except requests.exceptions.TooManyRedirects as too_many_redirects_error:
        too_many_redirects_error_line = "Too Many Redirects Error: {} \nURL: {}".format(too_many_redirects_error,
                                                                                        gallery_url)
        logger.error(too_many_redirects_error_line)
        print(too_many_redirects_error_line)
    except requests.exceptions.RequestException as request_exception:
        request_exception_line = "Request Exception: {} \nURL: {}".format(request_exception, gallery_url)
        logger.error(request_exception_line)
        print(request_exception_line)

    return False
