#!/usr/bin/env python3
"""Module for listing all documents in a MongoDB collection."""


def list_all(mongo_collection):
    """Lists all documents in a MongoDB collection.

    Args:
        mongo_collection: A pymongo collection object.

    Returns:
        A list of documents in the collection. If the collection is empty,
        an empty list is returned.
    """
    return [doc for doc in mongo_collection.find()]
