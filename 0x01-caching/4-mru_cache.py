#!/usr/bin/env python3
"""BasicCache Class implementation"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """A caching system that uses MRU replacement policy"""

    def __init__(self):
        """ Initiliaze
        """
        self.order = {}
        self.count = 0
        super().__init__()

    def put(self, key, item):
        """Assign to self.cache_data dictionary the key,item pairs

        If the number of items in self.cache_data is
        higher than BaseCaching.MAX_ITEMS it discards
        the most recently used item in cache
        """
        if key is None or item is None:
            return

        if (len(self.cache_data) == self.MAX_ITEMS
                and key not in self.cache_data):
            mru_keys = sorted(self.order.items(), key=lambda x: x[1])
            discarded_key = mru_keys[-1][0]
            del self.order[discarded_key]
            del self.cache_data[discarded_key]
            print(f'DISCARD: {discarded_key}')

        self.order[key] = self.count
        self.cache_data[key] = item
        self.count += 1

    def get(self, key):
        """Return the value in self.cache_data linked to key"""
        if key and key in self.cache_data:
            self.order[key] = self.count
            self.count += 1
            return self.cache_data[key]
