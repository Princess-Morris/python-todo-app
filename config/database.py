import urllib
from pymongo import MongoClient

from sqlalchemy import create_engine


# client = MongoClient(
# "mongodb+srv://princess:" + urllib.parse.quote("Osinachi@Princess") + "@cluster0.dlmqw0j.mongodb.net/?retryWrites=true&w=majority"
# )

client = MongoClient(
    "mongodb://localhost:27017/"
)

db = client.todo_db

collection_name = db["todo_collection"]

# collection_name.insert_one({"name": "Mike", "description": "a desc here", "complete": false})

# for name in collection_name.find():
#     print(name)