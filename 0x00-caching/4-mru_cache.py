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
            self.cache_data[key] = item

        dict_list = list(self.cache_data)
        lencache = len(self.cache_data)
        if (lencache > super().MAX_ITEMS):
            del self.cache_data[dict_list[super().MAX_ITEMS - 1]]
            print("DISCARD:", dict_list[super().MAX_ITEMS - 1])

    def get(self, key):
        """Retrieves the key value of an item"""
        if key and self.cache_data.get(key):
            return self.cache_data.get(key)
        else:
            return None
