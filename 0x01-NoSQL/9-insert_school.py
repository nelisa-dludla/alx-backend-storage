#!/usr/bin/env python3
'''
This function inserts a new document
in a collection based on kwargs
'''

from pymongo.collection import Collection
from typing import Dict


def insert_school(mongo_collection: Collection, **kwargs: Dict):
    '''
    Inserts a new document into a collection
    '''
    document = {}
    for k, v in kwargs.items():
        document[k] = v

    result = mongo_collection.insert_one(document)
    return result.inserted_id
