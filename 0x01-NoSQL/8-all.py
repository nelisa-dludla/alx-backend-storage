#!/usr/bin/env python3
'''This function lists all documents in a collection'''
from pymongo.collection import Collection
from typing import List


def list_all(mongo_collection: Collection) -> List[dict]:
    '''Returns a list of documents in a collection'''

    documents = mongo_collection.find()
    documents_list = list(documents)

    if documents_list:
        return documents_list
    else:
        return []
