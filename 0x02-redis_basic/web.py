#!/usr/bin/env python3
"""
Module with tools for request caching and tracking using Redis.
"""

import redis
import requests
from functools import wraps
from typing import Callable

# Initialize a Redis instance for caching and tracking
redis_store = redis.Redis()


def data_cacher(method: Callable) -> Callable:
    """Decorator to cache the output of a function and track request count.

    Args:
        method (Callable): The function whose output is to be cached.

    Returns:
        Callable: The wrapped function with caching and tracking.
    """
    @wraps(method)
    def invoker(url) -> str:
        """
        Caches the result of the URL fetch and tracks the request count.

        Args:
            url (str): The URL to fetch data from.

        Returns:
            str: The content of the URL, either from cache or fetched anew.
        """
        redis_store.incr(f'count:{url}')
        result = redis_store.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        result = method(url)
        redis_store.set(f'count:{url}', 0)
        redis_store.setex(f'result:{url}', 10, result)
        return result
    return invoker


@data_cacher
def get_page(url: str) -> str:
    """
    Fetches and returns the content of a URL, with caching.

    Args:
        url (str): The URL to fetch data from.

    Returns:
        str: The content of the URL.
    """
    return requests.get(url).text
