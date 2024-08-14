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
    def invoker(url: str) -> str:
        """
        Caches the result of the URL fetch and tracks the request count.

        Args:
            url (str): The URL to fetch data from.

        Returns:
            str: The content of the URL, either from cache or fetched anew.
        """
        # Increment the access count for the URL
        redis_store.incr(f'count:{url}')

        # Attempt to get cached result
        result = redis_store.get(f'result:{url}')
        if result:
            return result.decode('utf-8')

        # Fetch the result from the URL if not cached
        try:
            result = method(url)
        except requests.RequestException as e:
            return f"An error occurred: {e}"

        # Cache the result with an expiration time of 10 seconds
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
    response = requests.get(url)
    response.raise_for_status()
    return response.text


# Example usage (for testing purposes):
if __name__ == "__main__":
    test_url = (
        "http://slowwly.robertomurray.co.uk/delay/3000/url/"
        "http://www.google.com"
    )
    print(get_page(test_url))
    access_count = redis_store.get(f'count:{test_url}').decode('utf-8')
    print(f"Access count for {test_url}: {access_count}")
