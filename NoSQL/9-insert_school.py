#!/usr/bin/env python3
"""documentation"""
import pymongo

def insert_school(mongo_collection, **kwargs):
    """documentation"""


    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
