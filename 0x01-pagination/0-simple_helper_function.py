#!/usr/bin/env python3
"""Helper function to get a range of indexes of a page.
Takes two arguments, page and page_size which determine
which page the program is currently on, as well as how large the page is
The function returns these values as a tuple"""


def index_range(page, page_size):
    """returns starting page and ending page based on page index and size"""
    if page and page_size:
        start_point = (page - 1) * page_size
        end_point = start_point + page_size
        return start_point, end_point
