#!/usr/bin/env python3
"""BasicCache Class implementation"""
from base_caching import BaseCaching
from collections import deque


class FIFOCache(BaseCaching):
    """A caching system that uses FIFO replacement policy"""

    def __init__(self):
        """ Initiliaze
        """
        self.q = deque()
        super().__init__()

    def put(self, key, item):
        """Assign to self.cache_data dictionary the key,item pairs

        If the number of items in self.cache_data is
        higher than BaseCaching.MAX_ITEMS it discards
        the first item put in cache
        """
        if key is None or item is None:
            return

        if (len(self.cache_data) == self.MAX_ITEMS
                and key not in self.cache_data):
            discarded_key = self.q.popleft()
            del self.cache_data[discarded_key]
            print(f'DISCARD: {discarded_key}')
        if key not in self.cache_data:
            self.q.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Return the value in self.cache_data linked to key"""
        if key:
            return self.cache_data.get(key, None)
