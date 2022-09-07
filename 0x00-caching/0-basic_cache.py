#!/usr/bin/python3
"""BasicCache module which gets the value of a key item pair or puts a key value"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class inherits methods and attributes from BaseCaching class"""


    def put(self, key, item):
        """Assigns a key value to an item in cache_data"""
        if key and item:
            self.cache_data[key] = item



    def get(self, key):
        """Gets a key value from cache_data and displays it"""

        if key and self.cache_data.get(key):
            return self.cache_data.get(key)
        else:
            return None
