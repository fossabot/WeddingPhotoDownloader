#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Module that runs the script """
try:
    import sys
    from argparse import ArgumentParser, Namespace
    from src.logger import setup_logging, logger
except ModuleNotFoundError:
    print('Something went wrong while importing dependencies. Please, check the requirements file')
    sys.exit(1)


def main() -> None:
    """ Main function that executes the script """

    setup_logging()

    parser = ArgumentParser(description='Get the wedding photos and videos from the web gallery')
    subparsers = parser.add_subparsers(title='Commands', dest='command')
    subparser = subparsers.add_parser('download', help='Download the web gallery')
    subparser.add_argument('--gallery', type=str, required=True, help="Identifier of the web gallery")

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
    logger.info('Processing arguments')

    command = arguments.command
    if command == 'download':
        gallery_identifier = arguments.gallery
    else:
        logger.error(f"Command {command} is not recognised")


if __name__ == '__main__':
    main()
