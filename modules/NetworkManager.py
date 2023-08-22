# -*- coding: utf-8 -*-
""" Module in charge of network requests """

try:
    import requests
    import sys
    from pathlib import Path
    from typing import Any
    from modules.StorageManager import write_item_to_disk
    from resources.configuration import WEEDING_WEBSITE_BASE_URL, WEB_REQUESTS_HEADERS, IMAGE_GIF_REQUESTS_HEADERS
    from resources.configuration import VIDEO_PAYLOAD, VIDEO_REQUESTS_HEADERS, IMAGE_GIF_CDN_PREFIX_URL
    from resources.configuration import VIDEO_CDN_PREFIX_URL
    from utils.Messages import handle_info_message, handle_error_message, handle_warning_message
    from utils.GalleryItem import GalleryItem
except ModuleNotFoundError:
    print("Something went wrong while importing dependencies. Please, check the requirements file")
    sys.exit(1)


def make_http_request(url: str, headers: dict[str, str], parameters: dict[str, str] = None) -> tuple[bool, Any]:
    """
    It makes a web request and returns the response

    :param str url: The code of the gallery to download
    :param dict[str, str] headers: The headers to be used in the request
    :param dict[str, str] parameters: The parameters to be used in the request, if necessary
    :return: A tuple, where the first value is a bool indicating whether the request was successful and the second value
    is the response object or None
    :rtype: bool
    """
    handle_info_message(f"Making a web request to {url} ")

    try:
        if parameters is not None:
            response = requests.get(url, headers=headers, stream=True, params=parameters)
        else:
            response = requests.get(url, headers=headers, stream=True)
        return True, response
    except requests.exceptions.HTTPError as http_error:
        handle_error_message(f"HTTP Error: {http_error} \nURL: {url}")
    except requests.exceptions.ConnectionError as connection_error:
        handle_error_message(f"Error Connecting: {connection_error} \nURL: {url}")
    except requests.exceptions.Timeout as timeout_error:
        handle_error_message(f"Timeout Error: {timeout_error} \nURL: {url}")
    except requests.exceptions.TooManyRedirects as too_many_redirects_error:
        handle_error_message(f"Too Many Redirects Error: {too_many_redirects_error} \nURL: {url}")
    except requests.exceptions.RequestException as request_exception:
        handle_error_message(f"Request Exception: {request_exception} \nURL: {url}")

    return False, None


def check_gallery_availability(code: str) -> bool:
    """
    Check if the gallery corresponding to the received code exists or is available

    :param str code: The code of the gallery to download
    :return: True if the website pointed to by the URL exists or is available, False otherwise
    :rtype: bool
    """
    handle_info_message(f"Checking if the {code} gallery is available")

    gallery_url = ''.join([WEEDING_WEBSITE_BASE_URL, code])
    success, response = make_http_request(gallery_url, WEB_REQUESTS_HEADERS)
    if success and response.status_code == requests.codes['ok']:
        handle_info_message(f"The {code} gallery exists and is available")
        return True
    else:
        return False


def download_gallery_items(code: str, items: list[GalleryItem], download_folder: Path) -> None:
    """
    Downloads all the items from the gallery

    :param str code: The code of the gallery to download
    :param list[GalleryItem] items: A list with information about all the items of the gallery
    :param Path download_folder: The path to the folder where the items will be downloaded
    """
    handle_info_message(f"Beginning to download items from gallery {code}. Please, wait...")

    for item in items:
        headers, parameters = __get_item_headers_params(item.url)
        if headers is not None:
            if parameters is not None:
                success, response = make_http_request(item.url, headers, parameters)
            else:
                success, response = make_http_request(item.url, headers)
            if success and response.status_code == requests.codes['ok']:
                filename = __generate_sanitised_file_name(item.date, item.item_hash, item.file_type)
                full_path = Path(download_folder, filename)
                write_item_to_disk(full_path, response)
            else:
                handle_warning_message(f"The {item.url} item could not be downloaded. A {response.status_code} code has"
                                       f"been received")
        else:
            continue

    handle_info_message("The items obtained have been saved to disk")


def __generate_sanitised_file_name(item_date: str, item_hash: str, item_file_type: str) -> str:
    """
    Generates the sanitised file name

    :param str item_date: The date property of item to download
    :param str item_hash: The hash property of item to download
    :param str item_file_type: The file type property of item to download
    :return: The sanitised name, consisting of the date and hash separated by a hyphen with spaces
    :rtype: str
    """
    handle_info_message(f"Creating the item name with hash {item_hash}")

    sanitised_date = item_date.replace(':', '_')
    date_name_part = ' - '.join([sanitised_date, item_hash])
    return '.'.join([date_name_part, item_file_type])


def __get_item_headers_params(item_url: str) -> tuple[Any, Any]:
    """
    Gets the headers and payload of the item type

    :param str item_url: The URL of the gallery item to download
    :return: A tuple, where the first value is the headers to be used in the request and the second value is the
    payload. None for the first value if the item type is not recognised and for the second value if it is not needed
    :rtype: tuple[dict[str, str] or None, dict[str, str] or None]
    """
    handle_info_message(f"Detecting the item type for the URL {item_url}")

    if item_url.startswith(IMAGE_GIF_CDN_PREFIX_URL):
        return IMAGE_GIF_REQUESTS_HEADERS, None
    elif item_url.startswith(VIDEO_CDN_PREFIX_URL):
        return VIDEO_REQUESTS_HEADERS, VIDEO_PAYLOAD
    else:
        handle_warning_message(f"The item type for URL {item_url} is not supported")
        return None, None
