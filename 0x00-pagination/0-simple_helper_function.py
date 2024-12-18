#!/usr/bin/env python3
"""
A module that defines a helper function that
calculates the start and end indexes
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculates the start and end indexes given the page and page size

    Args:
        page (int): The page number(1-indexed, the first page is page 1.)
        page_size (int): The page size
    Returns:
        a tuple of size two containing a start index and an end index
        corresponding to the range of indexes to return in a list for
        those particular pagination parameters
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
