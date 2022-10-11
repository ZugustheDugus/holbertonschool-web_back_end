#!/usr/bin/env python3
"""
Cache class used to store data in a Redis
"""

import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def call_history(method: Callable) -> Callable:
    """Store the history of inputs and outputs for a particular function"""
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Union[str, int]:
        """Wrapper function"""
        self._redis.rpush(method.__qualname__ + ":inputs", str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(method.__qualname__ + ":outputs", str(output))
        return output
    return wrapper


def count_calls(method: Callable) -> Callable:
    """Counts how many methods of the Cache class are called"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Union[str, int]:
        """Wrapper function"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """
    Cache class which stores data in Redis
    """

    def __init__(self):
        """
        Constructor
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        t takes a data argument and returns a string. The method should
        generate a random key (e.g. using uuid), store the input data in
        Redis using the random key and return the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        Method that takes a key string argument and an optional
        Callable argument named fn. The method should return the
        value in Redis stored at the key. If fn is provided, the
        method should return fn(get(key)).
        """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """ automatically parametrize Cache.get to str """
        data = self._redis.get(key)
        return data.decode("utf-8")

    def get_int(self, key: str) -> int:
        """ automatically parametrize Cache.get to int """
        data = self._redis.get(key)
        return int(data)


def replay(method: Callable) -> None:
    """
    Method takes a single method argument and displays the name of the
    method, then the history of inputs and outputs for that method.
    """
    r = redis.Redis()
    qual_Name = method.__qualname__
    inputs = r.lrange(f"{qual_Name}:inputs", 0, -1)
    outputs = r.lrange(f"{qual_Name}:outputs", 0, -1)
    print("{} was called {} times:".format(qual_Name, len(inputs)))
    for i, o in zip(inputs, outputs):
        print(f"{qual_Name}(*{(i).decode('utf-8')}) -> {(o).decode('utf-8')}")
