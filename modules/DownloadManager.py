# -*- coding: utf-8 -*-
""" Module in charge of downloading the elements of the web gallery """

try:
    import sys
    from src.logger import logger
    from selenium.webdriver.support.wait import WebDriverWait
    from resources.configuration import WEEDING_WEBSITE_BASE_URL, REQUESTS_HEADERS
    from utils.FirefoxConfigurator import configure_firefox_options
    from utils.Messages import handle_info_message
    from selenium import webdriver
except ModuleNotFoundError:
    print("Something went wrong while importing dependencies. Please, check the requirements file")
    sys.exit(1)


class DownloadManager(object):
    """ The download manager """

    def __init__(self) -> None:
        self.url = WEEDING_WEBSITE_BASE_URL
        self.headers = REQUESTS_HEADERS
        self.driver = webdriver.Firefox(options=configure_firefox_options())
        self.web_driver_wait = WebDriverWait(self.driver, timeout=10, poll_frequency=1, ignored_exceptions=[])

    def scroll_to_bottom(self, code: str) -> bool:
        """
        Scrolls down until all items in the gallery are loaded

        :param str code: The code of the gallery to download
        :return: True if it was possible to move to the end of the gallery, False otherwise
        :rtype: bool
        """
        handle_info_message(f"Trying to reach the end of the {code} gallery")

    def exit(self) -> None:
        """
        Close the browser instance
        """
        handle_info_message("Closing the downloader")

        self.driver.quit()
