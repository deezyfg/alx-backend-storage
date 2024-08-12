#!/usr/bin/env python3
"""Module for retrieving top students from a MongoDB collection."""


def top_students(mongo_collection):
    """Retrieve students sorted by average score.

    Args:
        mongo_collection: The pymongo collection to query.

    Returns:
        A cursor to the sorted list of students.
    """
    students = mongo_collection.aggregate(
        [
            {
                '$project': {
                    '_id': 1,
                    'name': 1,
                    'averageScore': {
                        '$avg': {
                            '$avg': '$topics.score',
                        },
                    },
                    'topics': 1,
                },
            },
            {
                '$sort': {'averageScore': -1},
            },
        ]
    )
    return students
