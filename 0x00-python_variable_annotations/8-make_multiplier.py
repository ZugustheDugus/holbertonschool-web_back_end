#!/usr/bin/env python3
''' Returns a function that multiplies a given float by the
given multiplier, type annotated'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Returns the function to multiply input by multiplier'''
    def multiply_this(input: float) -> float:
        '''Returns input multiplied by multiplier'''
        return input * multiplier
    return multiply_this
