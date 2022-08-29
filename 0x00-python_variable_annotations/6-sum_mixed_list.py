#!/usr/bin/env python3
"""function to take mixed lists of floats and ints and return as a float"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns a float from the mixed list of ints and floats"""
    return sum(mxd_lst)
