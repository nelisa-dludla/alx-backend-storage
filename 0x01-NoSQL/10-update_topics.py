#!/usr/bin/env python3
'''
This Python function that changes all topics
of a school document based on the name
'''

from pymongo.collection import Collection
from typing import List


def update_topics(mongo_collection: Collection, name: str, topics: List[str]):
    '''
    Changes all topics of a school document
    '''
    filter_query = {'name': name}
    update_query = {'$set': {'topics': topics}}

    mongo_collection.update_one(filter_query, update_query)
