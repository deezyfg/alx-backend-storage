#!/usr/bin/env python3
"""Module for analyzing Nginx logs stored in MongoDB."""
from pymongo import MongoClient


def print_nginx_request_logs(nginx_collection):
    """Print statistics about Nginx request logs.

    Args:
        nginx_collection: The pymongo collection containing Nginx logs.
    """
    print('{} logs'.format(nginx_collection.count_documents({})))
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        req_count = len(list(nginx_collection.find({'method': method})))
        print('\tmethod {}: {}'.format(method, req_count))
    status_checks_count = len(list(
        nginx_collection.find({'method': 'GET', 'path': '/status'})
    ))
    print('{} status check'.format(status_checks_count))


def run():
    """Retrieve and print statistics about Nginx logs from MongoDB.

    Connects to the MongoDB server, accesses the Nginx logs collection,
    and prints statistics about request methods and status checks.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    print_nginx_request_logs(client.logs.nginx)


if __name__ == '__main__':
    run()
