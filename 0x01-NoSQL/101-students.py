#!/usr/bin/env python3
'''
This function returns all students sorted by average score
'''


def top_students(mongo_collection):
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
