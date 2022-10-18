#!/usr/bin/env python3
""" changes all topics of school document by name"""

from pymongo import MongoClient

def update_topics(mongo_collection, name, topics):
    """ changes all topics of school document by name"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
