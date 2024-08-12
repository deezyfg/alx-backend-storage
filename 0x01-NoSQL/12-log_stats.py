#!/usr/bin/env python3
"""Module for retrieving statistics from Nginx logs stored in MongoDB."""

from pymongo import MongoClient


def print_nginx_stats():
    """Prints statistics about Nginx logs from MongoDB."""
    # Connect to MongoDB and access the nginx collection
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # Count total number of log entries
    total_logs = nginx_collection.count_documents({})
    print(f'{total_logs} logs')

    # Count log entries for each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('Methods:')
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f'\tmethod {method}: {count}')

    # Count GET requests to the /status path
    status_check_count = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f'{status_check_count} status check')


if __name__ == "__main__":
    print_nginx_stats()
