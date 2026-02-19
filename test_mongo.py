
import urllib.parse
from pymongo.mongo_client import MongoClient
import os

uri = os.getenv("MONGO_DB_URL")
client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(f"Unable to connect to MongoDB: {e}")
