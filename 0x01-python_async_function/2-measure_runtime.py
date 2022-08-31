#!/usr/bin/env python3
'''Function which measures the time it takes for async tasks to complete'''

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''Starts a timer for the tasks and returns the final time'''
    startTime = time.time()
    asyncio.run(wait_n(n, max_delay))
    endTime = time.time()
    return (endTime - startTime) / n
