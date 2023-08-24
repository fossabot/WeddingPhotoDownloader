# -*- coding: utf-8 -*-
""" Represents an element of the gallery """


class GalleryItem(object):
    """ An element of the gallery """

    def __init__(self, item_hash: str = '', url: str = '', size: str = '', file_type: str = '', date: str = '') -> None:
        self.item_hash = item_hash
        self.url = url
        self.size = size
        self.file_type = file_type
        self.date = date

    def __str__(self) -> str:
        return (f"Hash: {self.item_hash}\nURL: {self.url}\nSize: {self.size}\nType: {self.file_type}\n"
                f"Date: {self.date}\n")
