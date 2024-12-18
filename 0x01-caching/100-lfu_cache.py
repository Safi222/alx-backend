#!/usr/bin/env python3
"""BasicCache Class implementation"""
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """A caching system that uses LFU replacement policy"""

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.frequency = {}

    def put(self, key, item):
        """Assign to self.cache_data dictionary the key,item pairs

        If the number of items in self.cache_data is
        higher than BaseCaching.MAX_ITEMS it discards
        the least frequency used item in cache
        """
        if key is None or item is None:
            return

        if (key not in self.cache_data
                and len(self.cache_data) == self.MAX_ITEMS):
            min_freq = min(self.frequency.values())
            potential_keys = [k for k, v in self.frequency.items()
                              if v == min_freq]

            discarded_key = None
            for k in self.cache_data:
                if k in potential_keys:
                    discarded_key = k
                    break

            del self.frequency[discarded_key]
            del self.cache_data[discarded_key]
            print(f'DISCARD: {discarded_key}')

        if key in self.cache_data:
            self.frequency[key] += 1
            self.cache_data.move_to_end(key)
        else:
            self.frequency[key] = 1
        self.cache_data[key] = item

    def get(self, key):
        """Return the value in self.cache_data linked to key"""
        if key and key in self.cache_data:
            self.frequency[key] += 1
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
