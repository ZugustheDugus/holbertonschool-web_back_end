#!/usr/bin/env python3
"""Async function to wait for a random amount of time"""


import asyncio
import random


async def wait_random(max_delay: int = 10):
    """Wait for a random number of seconds and return the time delay value"""
    random_delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
