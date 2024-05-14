#!/usr/bin/env python3
'''
This function returns all students sorted by average score
'''

import pymongo
from pymongo.collection import Collection


def top_students(mongo_collection: Collection):
    '''
    Returns all students sorted by average score
    '''
    pipeline = [
            {
                '$project': {
                    'name': '$name',
                    'averageScore': {'$avg': '$topics.score'},
                    }
            },
            {
                '$sort': {'averageScore': -1}
            }
        ]

    top_students = mongo_collection.aggregate(pipeline)
    top_students_list = list(top_students)

    return top_students_list
