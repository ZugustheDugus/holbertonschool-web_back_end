#!/usr/bin/env python3
''' This coroutine measures the time it takes to run async_comprehension
4 times in parallel using asyncio.gather. '''

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    ''' Uses asyncio.gather to run async_comprehension 4 times and
    returns the time it takes to run. '''
    startTime: float = time.time()
    await asyncio.gather(*[async_comprehension() for x in range(4)])
    endTime: float = time.time()
    return endTime - startTime
