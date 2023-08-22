# -*- coding: utf-8 -*-
""" Module in charge of disk operations """

try:
    import sys
    from pathlib import Path
    from requests import Response
    from tqdm import tqdm
    from resources.configuration import DOWNLOADS_PARENT_FOLDER
    from utils.Messages import handle_info_message, handle_error_message
except ModuleNotFoundError:
    print("Something went wrong while importing dependencies. Please, check the requirements file")
    sys.exit(1)


def create_download_folder(name: str, gallery: str) -> tuple[bool, Path]:
    """
    Create the folder to store the content of the gallery

    :param str name: The name of the folder where the downloads will be saved
    :param str gallery: The identifier of the gallery where its items will be saved
    :return: A tuple, where the first value is a bool indicating whether the folder could be created and the second
    value is the path to the folder
    :rtype: tuple[bool, Path]
    """
    handle_info_message("Trying to create the download folder")

    download_folder = Path().home().joinpath(DOWNLOADS_PARENT_FOLDER).joinpath(name).joinpath(gallery)
    try:
        Path(download_folder).mkdir(parents=True, exist_ok=True)
        handle_info_message("Download folder successfully created")
        return True, download_folder
    except OSError as exception:
        handle_error_message(f"Error creating the download folder: {exception}")
        return False, download_folder


def write_item_to_disk(item_path: Path, response: Response) -> bool:
    """
    Saves a gallery item to disk

    :param Path item_path: The path of the item to be saved to disk
    :param Response response: The response object of the request to obtain the item
    :return: True if it was possible to save the item to disk, False otherwise.
    :rtype: bool
    """
    handle_error_message(f"Saving item {item_path.name} to disk")

    total_size = int(response.headers.get('content-length', 0))
    try:
        with open(item_path, 'wb') as file, tqdm(desc=item_path.name, total=total_size, unit='iB', unit_scale=True,
                                                 unit_divisor=1024) as progress_bar:
            for data in response.iter_content(chunk_size=1024):
                size = file.write(data)
                progress_bar.update(size)

        return True
    except OSError as exception:
        handle_error_message(f"Error saving item {item_path.name} to disk: {exception.errno}")
        return False
