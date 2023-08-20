#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Module that runs the script """
try:
    import sys
    from argparse import ArgumentParser, Namespace
    from modules.DownloadManager import DownloadManager
    from src.logger import setup_logging, logger
    from modules.NetworkManager import check_gallery_availability
    from modules.StorageManager import create_download_folder
except ModuleNotFoundError:
    print("Something went wrong while importing dependencies. Please, check the requirements file")
    sys.exit(1)


def main() -> None:
    """ Main function that executes the script """

    setup_logging()

    parser = ArgumentParser(description="Get the wedding photos and videos from the web gallery")
    subparsers = parser.add_subparsers(title='Commands', dest='command')
    subparser = subparsers.add_parser(name='download', help="Download the web gallery")
    subparser.add_argument('--gallery', type=str, required=True, help="Identifier of the web gallery")
    subparser.add_argument('--name', type=str, required=True,
                           help="Name of the folder where the items will be downloaded")

    arguments = parser.parse_args()
    if arguments.command:
        process_arguments(arguments)
    else:
        parser.print_help()


def process_arguments(arguments: Namespace) -> None:
    """
    Processes the received arguments and starts the download process

    :param Namespace arguments: The arguments received
    """
    logger.info("Processing arguments")

    command = arguments.command
    if command == 'download':
        gallery_identifier = arguments.gallery.strip()
        folder_name = arguments.name.strip()
        gallery_available = check_gallery_availability(gallery_identifier)
        folder_created, folder_path = create_download_folder(folder_name)

        # The download manager creates the Firefox instance and starts the driver when it is initialised, as this
        # is a very expensive operation we only do it if the gallery is available and the folder could be created
        if gallery_available and folder_created:
            download_manager = DownloadManager()
            download_manager.exit()
        else:
            warning_lines = []
            if not gallery_available:
                warning_line = f"The {gallery_identifier} gallery does not exist or is currently unavailable"
                warning_lines.append(warning_line)
            if not folder_created:
                warning_line = f"The {folder_path} folder could not be created"
                warning_lines.append(warning_line)

            for warning_line in warning_lines:
                logger.warning(warning_line)
                print(warning_line)
    else:
        error_line = f"Command {command} is not recognised"
        logger.error(error_line)
        print(error_line)


if __name__ == '__main__':
    main()
