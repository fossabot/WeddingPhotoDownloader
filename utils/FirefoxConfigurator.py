# -*- coding: utf-8 -*-
""" Module that configures the Firefox instance """
try:
    import sys
    from selenium.webdriver.firefox.options import Options
    from resources.configuration import BROWSER_SILENT_MODE
    from src.logger import logger
except ModuleNotFoundError:
    print('Something went wrong while importing dependencies. Please, check the requirements file')
    sys.exit(1)


def configure_firefox_options() -> Options:
    """
    Configure the options with which to start Firefox

    :return: The specified configuration
    :rtype: Options
    """
    logger.info('Setting Firefox preferences')

    options = Options()
    # Run Firefox with no GUI
    if BROWSER_SILENT_MODE:
        options.add_argument('--headless')
    # Only cookies from the originating server are allowed
    options.set_preference('network.cookie.cookieBehavior', 1)
    # Disable Web Push Notifications Prompt
    options.set_preference("dom.webnotifications.enabled", False)
    options.set_preference("dom.push.enabled", False)

    return options
