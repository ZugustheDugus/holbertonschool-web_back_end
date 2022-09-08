#!/usr/bin/python3
"""Most Recently Used module for caching data"""


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUcache class inherits from BaseCaching"""

    def __init__(self):
        """Inits the module"""
        self = super().__init__()

    def put(self, key, item):
        """Adds item to cache. Deletes MRU item in cache if too many"""
        if key and item:
            if key in self.cache_data:
                self.cache_data.pop(key)
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                dict_list = list(self.cache_data)
                del_key = dict_list[self.MAX_ITEMS - 1]
                self.cache_data.pop(del_key)
                print("DISCARD:", del_key)

    def get(self, key):
        """Retrieves the key value of an item"""
        if key:
            item = self.cache_data.get(key)
            if item is not None:
                self.cache_data.pop(key)
                self.cache_data[key] = item
                return self.cache_data.get(key)
