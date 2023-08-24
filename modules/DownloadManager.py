# -*- coding: utf-8 -*-
""" Module in charge of downloading the elements of the web gallery """

try:
    import sys
    import time
    from selenium import webdriver
    from selenium.common import TimeoutException, NoSuchElementException, WebDriverException
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions
    from selenium.webdriver import FirefoxProfile
    from selenium.webdriver.support.wait import WebDriverWait
    from tqdm import tqdm
    from resources.configuration import WEEDING_WEBSITE_BASE_URL, WEB_REQUESTS_HEADERS, SCROLL_WAITING_TIME
    from resources.configuration import GALLERY_ITEMS_XPATH, GALLERY_ITEMS_CONTAINER_XPATH
    from utils.FirefoxConfigurator import configure_firefox_instance
    from utils.Messages import handle_info_message, handle_error_message, handle_critical_message
    from utils.GalleryItem import GalleryItem
except ModuleNotFoundError:
    print("Something went wrong while importing dependencies. Please, check the requirements file")
    sys.exit(1)


class DownloadManager(object):
    """ The download manager """

    def __init__(self) -> None:
        self.url = WEEDING_WEBSITE_BASE_URL
        self.headers = WEB_REQUESTS_HEADERS
        options, service = configure_firefox_instance()
        self.driver = webdriver.Firefox(options=options, service=service)
        self.web_driver_wait = WebDriverWait(self.driver, timeout=10, poll_frequency=1, ignored_exceptions=[])

    def scroll_to_bottom(self, code: str) -> bool:
        """
        Scrolls down until all items in the gallery are loaded

        :param str code: The code of the gallery to download
        :return: True if it was possible to move to the end of the gallery, False otherwise
        :rtype: bool
        """
        handle_info_message(f"Trying to reach the end of the {code} gallery. This might take a while, please wait...")

        try:
            self.driver.get(''.join([self.url, code]))
            self.web_driver_wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div[3]')))
            # Get scroll height.
            last_height = self.driver.execute_script("return document.body.scrollHeight")
            while True:
                # Scroll down to the bottom
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                # Wait for the elements to load and increase the height of the document
                time.sleep(SCROLL_WAITING_TIME)
                # Calculate new scroll height and compare with last scroll height
                new_height = self.driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                else:
                    last_height = new_height

            handle_info_message(f"End of {code} gallery reached, all elements have been loaded")
            return True
        except (TimeoutException, NoSuchElementException):
            handle_error_message(f"The DIV containing the {code} gallery elements could not be accessed")
        except WebDriverException:
            handle_critical_message(f"A fatal error has occurred, the execution of the script has been stopped:"
                                    f"{WebDriverException}")
            self.exit()
            sys.exit(1)

        return False

    def get_gallery_items_information(self, code: str) -> list[GalleryItem]:
        """
        Gets the information of the items in the gallery

        :param str code: The code of the gallery
        :return: A list with the information of the items found or empty if there are no items
        :rtype: list[GalleryItem]
        """
        handle_info_message(f"Getting the information of the items in the {code} gallery. Please, wait...")

        container_xpath_tuple = (By.XPATH, GALLERY_ITEMS_CONTAINER_XPATH)
        self.web_driver_wait.until(expected_conditions.element_to_be_clickable(container_xpath_tuple))
        gallery_items = self.driver.find_elements(By.XPATH, value=GALLERY_ITEMS_XPATH)
        total_items = len(gallery_items)
        handle_info_message(f"{total_items} items have been found in the gallery")

        items_data = []
        for gallery_item in tqdm(gallery_items):
            item_hash = gallery_item.get_attribute('data-hash')
            item_url = gallery_item.get_attribute('data-img')
            item_size = gallery_item.get_attribute('data-filesize')
            item_type = gallery_item.get_attribute('data-filetype')
            item_date = gallery_item.get_attribute('data-filecreated')
            new_item = GalleryItem(item_hash, item_url, item_size, item_type, item_date)
            items_data.append(new_item)

        handle_info_message(f"All information has been obtained from the items in the gallery {code}")
        return items_data

    def exit(self) -> None:
        """
        Close the browser instance
        """
        handle_info_message("Closing the downloader")

        self.driver.quit()
