#!/usr/bin/env python3
"""function to type variable 'k' and variable 'v' and adds them to a tuple"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """adds k and v to a tuple and returns"""
    return k, (v**2)
