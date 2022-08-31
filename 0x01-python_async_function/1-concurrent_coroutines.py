#!/usr/bin/env python3
'''Async funtion to run two async tasks simultaneously'''

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    '''Creates multiple tasks and appends them to a list as floats'''
    taskList = []
    resultList = []

    for x in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        taskList.append(task)

    for task in asyncio.as_completed(taskList):
        result: float = await task
        resultList.append(result)

    return resultList
