#!/usr/bin/env python3
'''
This function inserts a new document
in a collection based on kwargs
'''


def insert_school(mongo_collection, **kwargs):
    '''
    Inserts a new document into a collection
    '''
    document = {}
    for k, v in kwargs.items():
        document[k] = v

    result = mongo_collection.insert_one(document)
    return result.inserted_id
