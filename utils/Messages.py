# -*- coding: utf-8 -*-
""" Utility class to manage the script messages """

try:
    import sys
    from src.logger import logger
except ModuleNotFoundError:
    print("Something went wrong while importing dependencies. Please, check the requirements file")
    sys.exit(1)


def handle_info_message(message: str) -> None:
    """
     Handles INFO type messages

    :param str message: The message to be displayed and logged
    """

    logger.info(message)
    print(message)


def handle_warning_message(message: str) -> None:
    """
     Handles WARNING type messages

    :param str message: The message to be displayed and logged
    """

    logger.warning(message)
    print(message)


def handle_error_message(message: str) -> None:
    """
     Handles ERROR type messages

    :param str message: The message to be displayed and logged
    """

    logger.error(message)
    print(message)


def handle_critical_message(message: str) -> None:
    """
     Handles CRITICAL type messages

    :param str message: The message to be displayed and logged
    """

    logger.critical(message)
    print(message)
