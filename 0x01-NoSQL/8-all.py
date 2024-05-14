#!/usr/bin/env python3
'''This function lists all documents in a collection'''


def list_all(mongo_collection):
    '''Returns a list of documents in a collection'''

    documents = mongo_collection.find()
    documents_list = list(documents)

    if documents_list:
        return documents_list
    else:
        return []
