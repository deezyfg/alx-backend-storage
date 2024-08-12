#!/usr/bin/env python3
"""Module for retrieving schools by topic from a MongoDB collection."""

def schools_by_topic(mongo_collection, topic):
    """List schools with a specific topic.

    Args:
        mongo_collection: The pymongo collection to query.
        topic: The topic to filter schools by.

    Returns:
        A list of schools that have the specified topic.
    """
    top = {"topics": {"$elemMatch": {"$eq": topic}}}
    return [i for i in mongo_collection.find(top)]
