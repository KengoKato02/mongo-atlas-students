import random
from datetime import datetime, timedelta
from pymongo import MongoClient
from bson import ObjectId
from config import collection

def create_dummy_data(collection):
    # Create 10 users
    users = []
    for i in range(1, 11):
        user = {
            "_id": ObjectId(),
            "first_name": f"User{i}",
            "last_name": f"Lastname{i}",
            "email": f"user{i}@example.com",
            "password": f"encrypted_password_{i}",
            "createdAt": datetime.now() - timedelta(days=random.randint(1, 365))
        }
        users.append(user)
    
    collection.insert_many(users)

    # Create topics
    topics = [
        {"_id": ObjectId(), "title": "Python Basics", "description": "Introduction to Python", "createdAt": datetime.now(), "activities": []},
        {"_id": ObjectId(), "title": "Web Development", "description": "Learn web technologies", "createdAt": datetime.now(), "activities": []},
        {"_id": ObjectId(), "title": "Data Science", "description": "Explore data analysis", "createdAt": datetime.now(), "activities": []}
    ]

    # Create activities for each topic
    activity_types = ["quiz", "video", "exercise"]
    for topic in topics:
        for i in range(3):  # 3 activities per topic
            activity = {
                "_id": ObjectId(),
                "activity_type": random.choice(activity_types),
                "description": f"Activity {i+1} for {topic['title']}",
                "questions": [f"Question {j+1}" for j in range(3)],
                "url": f"http://example.com/{topic['title'].lower().replace(' ', '-')}/activity-{i+1}"
            }
            topic["activities"].append(activity["_id"])
            collection.insert_one(activity)

    collection.insert_many(topics)

    # Create progress and activity logs
    for user in users:
        progress = {
            "_id": ObjectId(),
            "user_id": user["_id"],
            "createdAt": datetime.now(),
            "topics": []
        }
        
        for topic in random.sample(topics, random.randint(1, len(topics))):
            progress["topics"].append(topic["_id"])
            
            for activity_id in random.sample(topic["activities"], random.randint(1, len(topic["activities"]))):
                activity_log = {
                    "_id": ObjectId(),
                    "user_id": user["_id"],
                    "activity_id": activity_id,
                    "start_time": datetime.now() - timedelta(hours=random.randint(1, 100)),
                    "end_time": datetime.now(),
                    "score": random.randint(0, 100)
                }
                collection.insert_one(activity_log)
        
        collection.insert_one(progress)

    print("Dummy data created successfully!")

create_dummy_data(collection)

def run_queries():
    # Perform your queries here
    print("Running queries...")
    # Example query:
    user_count = collection.count_documents({})
    print(f"Total number of users: {user_count}")