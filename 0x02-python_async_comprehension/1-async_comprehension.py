#!/usr/bin/env python3
''' This coroutine returns a list of the 10 random numbers generated
by async_generator. '''

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    ''' Uses async_generator to generate 10 random numbers between
    0-10 and then returns a list of those numbers. '''
    return [x async for x in async_generator()]
