#!/usr/bin/env python3
"""Async function to generate a random number between 0-10, 10 times"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    ''' Generates a number between 0 - 10 using random. 10 times.'''
    for x in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
