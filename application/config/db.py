import os

from pymongo import MongoClient


def get_db():
    mongo_uri = os.getenv("MONGO_URI")
    print("Connecting to:", mongo_uri)  # Debug log
    client = MongoClient(mongo_uri)
    return client["restaurant"]
