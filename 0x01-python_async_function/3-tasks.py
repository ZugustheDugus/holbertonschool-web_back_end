#!/usr/bin/env python3
'''Function to create an async task based on the random wait func'''

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''Returns the task and delay time in seconds'''
    return asyncio.create_task(wait_random(max_delay))
