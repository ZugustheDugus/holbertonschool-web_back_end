#!/usr/bin/env python3
""" Function to list all documents in a collection """


def list_all(mongo_collection):
    """Lists all documents as a collection"""
    if mongo_collection is not None:
        return mongo_collection.find()
    return []
