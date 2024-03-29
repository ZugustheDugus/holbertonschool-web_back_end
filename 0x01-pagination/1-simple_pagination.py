#!/usr/bin/env python3
"""Program to retrieve a specific set of pages from a server"""


import csv
import math
from typing import List


def index_range(page, page_size):
    """returns starting page and ending page based on page index and size"""
    if page and page_size:
        start_point = (page - 1) * page_size
        end_point = start_point + page_size
        return start_point, end_point


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Method to retrieve specific page(s)
        Asserts that both page and page_size are ints > 0"""
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        start, end = index_range(page, page_size)
        pages = []
        if start >= len(self.dataset()):
            return pages
        pages = self.dataset()
        return pages[start:end]
