#!/usr/bin/env python3
'''Function to wait n seconds to append tasks to a list'''

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    '''wait n seconds and appends tasks to list, returns time'''
    taskList = []
    resultList = []

    for x in range(n):
        task = task_wait_random(max_delay)
        taskList.append(task)

    for task in asyncio.as_completed(taskList):
        result: float = await task
        resultList.append(result)

    return resultList
