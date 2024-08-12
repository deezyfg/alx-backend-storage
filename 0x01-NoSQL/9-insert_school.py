#!/usr/bin/env python3
"""Module for inserting a document into a MongoDB collection."""


def insert_school(mongo_collection, **kwargs):
    """Inserts a document into a MongoDB collection.

    Args:
        mongo_collection: The pymongo collection to insert into.
        **kwargs: Document fields and values.

    Returns:
        The ID of the inserted document.
    """
    mon = mongo_collection.insert_one(kwargs)
    return mon.inserted_id
