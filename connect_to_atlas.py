import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

CONNECTION_STRING = os.getenv("MONGODB_URI")

if CONNECTION_STRING is None:
    raise ValueError("The environment variable MONGODB_URI is not set.")

client = MongoClient(CONNECTION_STRING)

db = client['students_tracker']
collection = db['students_tracker_collection']

sample_document = {"name": "Alice", "age": 25, "city": "New York"}
result = collection.insert_one(sample_document)

print(f"Inserted document with _id: {result.inserted_id}")

for doc in collection.find():
    print(doc)
