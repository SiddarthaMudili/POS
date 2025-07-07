from pymongo import MongoClient


def get_db():
    client = MongoClient("mongodb://mongo_host:27017/")
    return client["restaurant"]
