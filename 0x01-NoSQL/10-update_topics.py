#!/usr/bin/env python3
"""Module for updating topics in a MongoDB collection."""


def update_topics(mongo_collection, name, topics):
    """Update topics of documents with a specific name.

    Args:
        mongo_collection: The pymongo collection to update.
        name: The name of the documents to update.
        topics: The list of topics to set.

    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
