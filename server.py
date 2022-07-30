import pymongo
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["test"]
collection = db["test"]

mydict = {"_id": "cos", "name": "John", "address": "Highway 37" }

x = collection.insert_one(mydict)