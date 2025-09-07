import os
from pymongo import MongoClient

MONGODB_URI = os.getenv("MONGO_URI","mongodb://localhost:27017")

client = MongoClient(MONGODB_URI)
db = client[MONGODB_URI]