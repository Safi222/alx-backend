#!/usr/bin/env python3
"""
A module that defines a helper function that
calculates the start and end indexes
"""
import csv
import math
from typing import List, Tuple


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get the appropriate page of the dataset.

        Args:
            page (int): The page number(1-indexed, the first page is page 1.)
            page_size (int): The page size
        Returns:
            The appropriate page of the dataset(i.e. the correct list of rows).
        """
        assert (type(page) is int and type(page_size) is int)
        assert (page > 0 and page_size > 0)
        start, end = index_range(page, page_size)
        rows = self.dataset()
        if start < len(rows) and end <= len(rows):
            return rows[start: end]
        return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Get a dictionary containing info about the dataset.

        Args:
            page (int): The page number(1-indexed, the first page is page 1.)
            page_size (int): The page size
        Returns:
            A dictionary containing the following key-value pairs:
                page_size: the length of the returned dataset page
                page: the current page number
                data: the dataset page
                next_page: number of the next page, None if no next page
                prev_page: number of the previous page,
                           None if no previous page
                total_pages: the total number of pages in the dataset
        """
        total_pages = math.ceil(len(self.dataset()) / page_size)
        return {
                'page': page,
                'page_size': page_size,
                'data': self.get_page(page, page_size),
                'next_page': page + 1 if page + 1 <= total_pages else None,
                'prev_page': page - 1 if page > 1 else None,
                'total_pages': total_pages
                }
