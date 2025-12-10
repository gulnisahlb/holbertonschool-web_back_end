#!/usr/bin/env python3
"""documentation"""


def update_topics(mongo_collection, name, topics):
    """documentation"""


    mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics":topics}}
    )
