#!/usr/bin/python3
"""Least Recently Used module for caching data"""


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUcache class inherits from BaseCaching"""

    def __init__(self):
        """Inits the module"""
        self = super().__init__()

    def put(self, key, item):
        """Adds item to cache. Deletes LRU item in cache if too many"""
        if key and item:
            if key in self.cache_data:
                self.cache_data.pop(key)
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                dict_list = list(self.cache_data)
                del_key = dict_list[0]
                self.cache_data.pop(del_key)
                print("DISCARD:", del_key)

    def get(self, key):
        """Retrieves the key value of an item"""
        if key and self.cache_data.get(key):
            return self.cache_data.get(key)
        else:
            return None
