#!/usr/bin/env python3
'''
This function that returns the list
of school having a specific topic
'''


def schools_by_topic(mongo_collection, topic):
    '''
    Returns a list of schools having a specific topic
    '''
    filter_query = {'topics': {'$in': [topic]}}

    documents = mongo_collection.find(filter_query)
    documents_list = list(documents)

    return documents_list
