python3 -m pip install "pymongo[srv]"

python -m pip install python-dotenv

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