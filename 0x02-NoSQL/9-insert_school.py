#!/usr/bin/env python3
"""Inserts new document into collection based on kwargs"""

from pymongo import MongoClient

def insert_school(mongo_collection, **kwargs):
    """inserts new document into collection based on kwargs"""
    if mongo_collection is not None:
        return mongo_collection.insert_one(kwargs).inserted_id
    return []
