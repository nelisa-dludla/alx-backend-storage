#!/usr/bin/env python3
'''
This script that provides some stats
about Nginx logs stored in MongoDB
'''

import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['logs']
collection = db['nginx']

total_logs = collection.count_documents({})

print(f'{total_logs} logs')

print('Methods:')
methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
for method in methods:
    method_query = {'method': method}
    method_count = collection.count_documents(method_query)
    print(f'\tmethod {method}: {method_count}')

status_query = {'method': 'GET', 'path': '/status'}
status_count = collection.count_documents(status_query)
print(f'{status_count} status check')
