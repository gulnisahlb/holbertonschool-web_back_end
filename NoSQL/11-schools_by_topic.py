#!/usr/bin/env python3
"""documentation"""


def schools_by_topic(mongo_collection, topic):
    """documentation"""

    return list(mongo_collection.find({"topics":topic}))
