# -*- coding: utf-8 -*-
""" Configuration properties necessary for the operation of the script """

LOGS_FOLDER = 'logs'
# Available loggers: development, production
LOGS_MODE = 'production'
# Available levels: CRITICAL = 50, ERROR = 40, WARNING = 30, INFO = 20, DEBUG = 10
LOGS_LEVEL = 20

GECKODRIVER_LOG_NAME = 'geckodriver.log'

DOWNLOADS_PARENT_FOLDER = 'WeddingPhotoDownloads'

BROWSER_SILENT_MODE = True

SCROLL_WAITING_TIME = 2

__USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0'
__ACCEPT = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
__ACCEPT_LANGUAGE = 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3'

WEEDING_WEBSITE_BASE_URL = 'https://fotoshare.co/e/'
WEB_REQUESTS_HEADERS = {'Host': 'fotoshare.co', 'User-Agent': __USER_AGENT, 'Accept': __ACCEPT,
                        'Accept-Language': __ACCEPT_LANGUAGE, 'Accept-Encoding': 'gzip, deflate, br', 'DNT': '1',
                        'Connection': 'keep-alive', 'Upgrade-Insecure-Requests': '1', 'Sec-Fetch-Dest': 'document',
                        'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'TE': 'trailers', }

IMAGE_GIF_CDN_PREFIX_URL = 'https://cdnb.fotoshare.co/w/'
IMAGE_GIF_REQUESTS_HEADERS = {'Host': 'fotoshare-op.b-cdn.net', 'User-Agent': __USER_AGENT, 'Accept': __ACCEPT,
                              'Accept-Language': __ACCEPT_LANGUAGE, 'Accept-Encoding': 'gzip, deflate, br', 'DNT': '1',
                              'Connection': 'keep-alive', 'Upgrade-Insecure-Requests': '1',
                              'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'none',
                              'Sec-Fetch-User': '?1', }

VIDEO_CDN_PREFIX_URL = 'https://cdn-bz.fotoshare.co/lb/v/'
VIDEO_PAYLOAD = {'credentials': 'omit', 'mode': 'cors', }
VIDEO_REQUESTS_HEADERS = {'User-Agent': __USER_AGENT, 'Accept': __ACCEPT, 'Accept-Language': __ACCEPT_LANGUAGE,
                          'Upgrade-Insecure-Requests': '1', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate',
                          'Sec-Fetch-Site': 'cross-site', 'Pragma': 'no-cache', 'Cache-Control': 'no-cache', }

GALLERY_ITEMS_CONTAINER_XPATH = '/html/body/div[3]'

GALLERY_ITEMS_XPATH = "//div[@class='thumb']"

# See: https://github.com/mozilla/geckodriver/issues/2010
# Open a terminal and run '$ whereis geckodriver'
# geckodriver: /usr/bin/geckodriver /snap/bin/geckodriver
# If there is an option with 'SNAP' you have to specify that one, otherwise specify the one that appears
GECKODRIVER_PATH = '/snap/bin/geckodriver'
