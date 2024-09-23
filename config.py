import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

CONNECTION_STRING = os.getenv("MONGODB_URI")

if CONNECTION_STRING is None:
    raise ValueError("The environment variable MONGODB_URI is not set.")

client = MongoClient(CONNECTION_STRING)
db = client['students_tracker']
collection = db['students_tracker_collection']