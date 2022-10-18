#!/usr/bin/env python3
"""Log stats"""


if __name__ == "__main__":
    from pymongo import MongoClient
    client = MongoClient() # defaults to localhost:27017
    collection = client.logs.nginx # collection nginx in database logs

    print("{} logs".format(collection.count_documents({}))) # count all documents
    print("Methods:") 
    method_list = ["GET", "POST", "PUT", "PATCH", "DELETE"] # list of methods
    for method in method_list: 
        print("\tmethod {}: {}".format(method, collection.count_documents({"method": method}))) # count documents with method
    print("{} status check".format(collection.count_documents({"path": "/status"}))) # count documents with path /status
