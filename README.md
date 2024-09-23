## ER Diagram

![ER Diagram](/ER-Diagram.png)

## Relationships

### Many-to-Many: Users and Activity (via Activity Logs)
- Users and Activities have a many-to-many relationship through the Activity Logs table.
- A user can participate in multiple activities.
- Each activity can be performed by multiple users.
- The Activity Logs table acts as a join table.

### Many-to-Many: Users and Topics (via Progress)
- A user can be associated with multiple topics through their progress, and each topic can have progress tracked by multiple users.
- The Progress table acts as a join table that tracks which topics a user has made progress on.

### One-to-Many: Topics and Activity
- Each topic can have multiple activities, but each activity belongs to only one topic.

## Installation Setup

To get started with this project, you need to have the following installed:

1. **MongoDB**: You can download and install MongoDB from the [official MongoDB website](https://www.mongodb.com/try/download/community).

2. **Python**: Ensure you have Python installed. You can download it from the [official Python website](https://www.python.org/downloads/).

3. **Pip**: Pip is the package installer for Python. It should come pre-installed with Python. You can check if it's installed by running:
    ```bash
    python -m pip --version
    ```

4. **Virtual Environment**: It's recommended to use a virtual environment to manage your project dependencies. You can create a virtual environment by running:
    ```bash
    python -m venv venv
    ```

5. **Activate the Virtual Environment**:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```

6. **Install Required Packages**: Once the virtual environment is activated, install the required packages using pip:
    ```bash
    python -m pip install "pymongo[srv]"
    python -m pip install python-dotenv
    ```

## Setting Up the `.env` File

You need to create a `.env` file in the root directory of your project. This file will store your environment variables, including the MongoDB connection string.

1. **Create the `.env` File**: In the root directory of your project, create a file named `.env`.

2. **Add the MongoDB URI**: Open the `.env` file and add your MongoDB connection string. It should look something like this:
    ```env
    MONGODB_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority
    ```

    Replace `<username>`, `<password>`, and `<dbname>` with your actual MongoDB credentials and database name.

## Example Code

Here is an example of how you can use the `pymongo` and `python-dotenv` packages to connect to MongoDB and perform some basic operations:

```python:connect_to_atlas.py
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
```

This script loads the MongoDB URI from the `.env` file, connects to the MongoDB database, inserts a sample document, and prints all documents in the collection.

## Running the Script

To run the script, ensure your virtual environment is activated and then execute the script using Python:
```bash
python connect_to_atlas.py
```

This will insert a sample document into the MongoDB collection and print all documents in the collection to the console.