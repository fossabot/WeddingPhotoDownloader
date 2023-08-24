# -*- coding: utf-8 -*-
""" Utility class that configures the Firefox instance """

try:
    import sys
    from selenium.webdriver.firefox.service import Service
    from selenium.webdriver.firefox.options import Options
    from resources.configuration import BROWSER_SILENT_MODE, GECKODRIVER_PATH, GECKODRIVER_LOG_NAME
    from src.logger import get_log_path
    from utils.Messages import handle_info_message
except ModuleNotFoundError:
    print("Something went wrong while importing dependencies. Please, check the requirements file")
    sys.exit(1)


def configure_firefox_instance() -> tuple[Options, Service]:
    """
    Configure the service and the options with which to start Firefox

    :return: A tuple, where the first value is the options and the second is the service to be used
    :rtype: tuple[Options, Service]
    """
    handle_info_message("Configuring the Firefox instance")

    geckodriver_log_path = str(get_log_path().joinpath(GECKODRIVER_LOG_NAME).resolve())
    service = Service(executable_path=GECKODRIVER_PATH, log_output=geckodriver_log_path)
    options = Options()
    # Run Firefox with no GUI
    if BROWSER_SILENT_MODE:
        options.add_argument('--headless')
    # Only cookies from the originating server are allowed
    options.set_preference('network.cookie.cookieBehavior', 1)
    # Disable Web Push Notifications Prompt
    options.set_preference('dom.webnotifications.enabled', False)
    options.set_preference('dom.push.enabled', False)

    return options, service
