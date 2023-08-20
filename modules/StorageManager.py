# -*- coding: utf-8 -*-
""" Module in charge of disk operations """

try:
    import sys
    from pathlib import Path
    from resources.configuration import DOWNLOADS_PARENT_FOLDER
    from utils.Messages import handle_info_message, handle_error_message
except ModuleNotFoundError:
    print("Something went wrong while importing dependencies. Please, check the requirements file")
    sys.exit(1)


def create_download_folder(name: str) -> tuple[bool, Path]:
    """
    Create the folder to store the content of the gallery

    :param str name: The name of the folder where the downloads will be saved
    :return: A tuple, where the first value is a bool indicating whether the folder could be created and the second
    value is the path to the folder
    :rtype: tuple[bool, Path]
    """
    handle_info_message("Trying to create the download folder")

    download_folder = Path().home().joinpath(DOWNLOADS_PARENT_FOLDER).joinpath(name)
    try:
        Path(download_folder).mkdir(parents=True, exist_ok=True)
        handle_info_message("Download folder successfully created")
        return True, download_folder
    except OSError as exception:
        handle_error_message(f"Error creating the download folder: {exception.errno}")
        return False, download_folder
