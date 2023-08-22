#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Module that runs the script """

try:
    import sys
    from argparse import ArgumentParser, Namespace
    from pathlib import Path
    from modules.DownloadManager import DownloadManager
    from src.logger import setup_logging
    from modules.NetworkManager import check_gallery_availability, download_gallery_items
    from modules.StorageManager import create_download_folder
    from utils.Messages import handle_warning_message, handle_info_message, handle_error_message
except ModuleNotFoundError:
    print("Something went wrong while importing dependencies. Please, check the requirements file")
    sys.exit(1)


def main() -> None:
    """ Main function that executes the script """

    setup_logging()

    parser = ArgumentParser(description="Get the wedding photos and videos from the web gallery")
    subparsers = parser.add_subparsers(title='Commands', dest='command')
    subparser = subparsers.add_parser(name='download', help="Download the web gallery")
    subparser.add_argument('--gallery', type=str, nargs='+', required=True,
                           help="A list of gallery identifiers, separated by a space")
    subparser.add_argument('--name', type=str, required=True,
                           help="Name of the folder where the items will be downloaded")

    arguments = parser.parse_args()
    if arguments.command:
        process_arguments(arguments)
    else:
        parser.print_help()


def process_arguments(arguments: Namespace) -> None:
    """
    Processes the received arguments

    :param Namespace arguments: The arguments received
    """
    handle_info_message("Processing the arguments received")

    command = arguments.command
    if command == 'download':
        gallery_identifiers = arguments.gallery
        folder_name = arguments.name.strip()
        process_galleries(gallery_identifiers, folder_name)
    else:
        handle_error_message(f"Command {command} is not recognised")


def process_galleries(gallery_identifiers: list[str], folder_name: str) -> None:
    """
    Checks if the gallery is available and the download folder has been created, if so, starts downloading the gallery

    :param list[str] gallery_identifiers: The identifiers of the galleries to download
    :param str folder_name: The name of the folder where the downloads will be saved
    """

    for gallery_identifier in gallery_identifiers:
        gallery_available = check_gallery_availability(gallery_identifier)
        folder_created, folder_path = create_download_folder(folder_name, gallery_identifier)
        # The download manager creates the Firefox instance and starts the driver when it is initialised, as this
        # is a very expensive operation we only do it if the gallery is available and the folder could be created
        if gallery_available and folder_created:
            execute_downloader(gallery_identifier, folder_path)
        else:
            warning_lines = []
            if not gallery_available:
                warning_line = f"The {gallery_identifier} gallery does not exist or is currently unavailable"
                warning_lines.append(warning_line)
            if not folder_created:
                warning_line = f"The {folder_path} folder could not be created"
                warning_lines.append(warning_line)

            for warning_line in warning_lines:
                handle_warning_message(warning_line)


def execute_downloader(gallery_identifier: str, download_folder: Path) -> None:
    """
    Operates the download manager

    :param str gallery_identifier: The code of the gallery to download
    :param Path download_folder: The path to the folder where the items will be downloaded
    """

    download_manager = DownloadManager()
    download_manager.scroll_to_bottom(gallery_identifier)
    items_details = download_manager.get_gallery_items_information(gallery_identifier)
    # We have the information of all items (if they have been found). We do not need the browser instance anymore
    download_manager.exit()
    if items_details:
        download_gallery_items(gallery_identifier, items_details, download_folder)


if __name__ == '__main__':
    main()
