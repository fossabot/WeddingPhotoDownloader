# -*- coding: utf-8 -*-
""" Module in charge of network requests """

try:
    import requests
    import sys
    from resources.configuration import WEEDING_WEBSITE_BASE_URL, REQUESTS_HEADERS
    from utils.Messages import handle_info_message, handle_error_message
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
    handle_info_message(f"Checking if the {code} gallery is available")

    gallery_url = ''.join([WEEDING_WEBSITE_BASE_URL, code])
    try:
        response = requests.get(gallery_url, headers=REQUESTS_HEADERS)
        if response.status_code == requests.codes['ok']:
            handle_info_message(f"The {code} gallery exists and is available")
            return True
    except requests.exceptions.HTTPError as http_error:
        handle_error_message(f"HTTP Error: {http_error} \nURL: {gallery_url}")
    except requests.exceptions.ConnectionError as connection_error:
        handle_error_message(f"Error Connecting: {connection_error} \nURL: {gallery_url}")
    except requests.exceptions.Timeout as timeout_error:
        handle_error_message(f"Timeout Error: {timeout_error} \nURL: {gallery_url}")
    except requests.exceptions.TooManyRedirects as too_many_redirects_error:
        handle_error_message(f"Too Many Redirects Error: {too_many_redirects_error} \nURL: {gallery_url}")
    except requests.exceptions.RequestException as request_exception:
        handle_error_message(f"Request Exception: {request_exception} \nURL: {gallery_url}")

    return False
