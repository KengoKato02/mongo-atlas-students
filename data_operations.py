def create_dummy_data(collection):
    dummy_data = [
        {
            "name": "John Doe",
            "age": 30,
            "city": "New York",
            "skills": ["Python", "MongoDB"],
            "projects": [
                {"name": "Project A", "status": "completed"},
                {"name": "Project B", "status": "ongoing"}
            ]
        },
        {
            "name": "Jane Smith",
            "age": 28,
            "city": "San Francisco",
            "skills": ["JavaScript", "React"],
            "projects": [
                {"name": "Project C", "status": "ongoing"}
            ]
        },
        {
            "name": "Bob Johnson",
            "age": 35,
            "city": "Chicago",
            "skills": ["Java", "SQL"],
            "projects": [
                {"name": "Project D", "status": "completed"},
                {"name": "Project E", "status": "ongoing"},
                {"name": "Project F", "status": "planned"}
            ]
        }
    ]
    result = collection.insert_many(dummy_data)
    print(f"Inserted {len(result.inserted_ids)} documents")

def run_queries(collection):
    print("\nRunning queries:")
    
    print("\n1. All documents:")
    for doc in collection.find():
        print(doc)

    print("\n2. People older than 30:")
    for doc in collection.find({"age": {"$gt": 30}}):
        print(doc)

    print("\n3. People with both Python and MongoDB skills:")
    query = {"$and": [{"skills": "Python"}, {"skills": "MongoDB"}]}
    for doc in collection.find(query):
        print(doc)

    print("\n4. People in New York or aged 28:")
    query = {"$or": [{"city": "New York"}, {"age": 28}]}
    for doc in collection.find(query):
        print(doc)

    print("\n5. People with ongoing projects:")
    query = {"projects": {"$elemMatch": {"status": "ongoing"}}}
    for doc in collection.find(query):
        print(doc)

    count = collection.count_documents({"projects.1": {"$exists": True}})
    print(f"\n6. Number of people with more than one project: {count}")