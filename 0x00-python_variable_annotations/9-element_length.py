#!/usr/bin/env python3
'''Takes a given function and type anotates it'''

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Returns a list of tuples from lst'''
    return [(i, len(i)) for i in lst]
