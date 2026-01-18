
from pymongo import MongoClient
from settings import MONGO_URI, DB_NAME, COLLECTION_NAME


def get_cars_collection():
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    return db[COLLECTION_NAME]
