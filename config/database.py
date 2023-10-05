import urllib

from pymongo import MongoClient

client = MongoClient(
"mongodb+srv://princess:" + urllib.parse.quote("Osinachi@Princess") + "@cluster0.dlmqw0j.mongodb.net/?retryWrites=true&w=majority"
)

db = client.todo_db

collection_name = db["todo_collection"]