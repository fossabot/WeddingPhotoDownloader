# -*- coding: utf-8 -*-
""" Configuration properties necessary for the operation of the script """

LOGS_FOLDER = 'logs'
# Available loggers: development, production
LOGS_MODE = 'production'
# Available levels: CRITICAL = 50, ERROR = 40, WARNING = 30, INFO = 20, DEBUG = 10
LOGS_LEVEL = 20

REQUESTS_HEADERS = {'Host': 'fotoshare.co',
                    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                    'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3', 'Accept-Encoding': 'gzip, deflate, br',
                    'DNT': '1', 'Connection': 'keep-alive', 'Upgrade-Insecure-Requests': '1',
                    'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site',
                    'TE': 'trailers', }

WEEDING_WEBSITE_BASE_URL = 'https://fotoshare.co/e/'

DOWNLOADS_PARENT_FOLDER = 'WeddingPhotoDownloads'

BROWSER_SILENT_MODE = False
