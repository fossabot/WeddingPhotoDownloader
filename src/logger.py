# -*- coding: utf-8 -*-
""" Module that manages the LOG """
try:
    import sys
    import yaml
    import logging.config
    from logging import LogRecord
    from pathlib import Path
    from resources.configuration import LOGS_FOLDER, LOGS_LEVEL, LOGS_MODE
except ModuleNotFoundError:
    print("Something went wrong while importing dependencies. Please, check the requirements file")
    sys.exit(1)

__file_path = Path(__file__).resolve()
__root_folder = __file_path.parent.parent
__path_log_folder = Path(__root_folder).joinpath(LOGS_FOLDER)
__path_log_config_file = Path(__root_folder).joinpath('resources').joinpath('log.yaml')


class InfoFilter(logging.Filter):
    """ INFO level logging filter """

    def __init__(self) -> None:
        super().__init__()

    def filter(self, record: LogRecord) -> bool:
        """
        Filter the current log record

        :param LogRecord record: The actual log record
        :return: If the current log record is of INFO level
        :rtype: bool
        """
        return record.levelno == logging.INFO


class WarningFilter(logging.Filter):
    """ WARNING level logging filter """

    def __init__(self) -> None:
        super().__init__()

    def filter(self, record: LogRecord) -> bool:
        """
        Filter the current log record

        :param LogRecord record: The actual log record
        :return: If the current log record is of WARNING level
        :rtype: bool
        """
        return record.levelno == logging.WARNING


class ErrorFilter(logging.Filter):
    """ ERROR level logging filter """

    def __init__(self) -> None:
        super().__init__()

    def filter(self, record: LogRecord) -> bool:
        """
        Filter the current log record

        :param LogRecord record: The actual log record
        :return: If the current log record is of ERROR level
        :rtype: bool
        """
        return record.levelno == logging.ERROR


class CriticalFilter(logging.Filter):
    """ CRITICAL level logging filter """

    def __init__(self) -> None:
        super().__init__()

    def filter(self, record: LogRecord) -> bool:
        """
        Filter the current log record

        :param LogRecord record: The actual log record
        :return: If the current log record is of CRITICAL level
        :rtype: bool
        """
        return record.levelno == logging.CRITICAL


def create_logs_folder() -> bool:
    """
    Detects whether the log directory exists or not, if it does not exist it creates it

    :return: True if the folder exists or has been created, False if the folder could not be created
    :rtype: bool
    """

    if not Path(__path_log_folder).exists():
        try:
            Path(__path_log_folder).mkdir(exist_ok=True)
            return True
        except OSError:
            print(f"Creation of the log directory '{__path_log_folder}' failed")
            return False
    else:
        return True


def setup_logging() -> None:
    """ Initialise the logging system """

    if create_logs_folder():
        if Path(__path_log_config_file).exists():
            if Path(__path_log_config_file).is_file():
                with open(__path_log_config_file, 'rt') as config_file:
                    config = yaml.safe_load(config_file.read())
                    logging.config.dictConfig(config)
            else:
                print(f"The path to the log configuration file must be a file not a directory: "
                      f"{__path_log_config_file}")
        else:
            print(f"The path to the log configuration file do not exist: {__path_log_config_file}")
    else:
        print("An error occurred while trying to configure the logging system")


def get_log_path() -> Path:
    """
    Returns the path to the folder where the logs are stored

    :return: The path to the log folder
    :rtype: Path
    """

    return __path_log_folder


logger = logging.getLogger(LOGS_MODE)
logger.setLevel(LOGS_LEVEL)
