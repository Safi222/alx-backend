#!/usr/bin/env python3
"""BasicCache Class implementation"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A caching system that doesn’t have limit"""

    def put(self, key, item):
        """Assign to self.cache_data dictionary the key,item pairs"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Return the value in self.cache_data linked to key"""
        if key:
            return self.cache_data.get(key, None)
