
import urllib.parse
from pymongo.mongo_client import MongoClient



escaped_username = urllib.parse.quote_plus("dsh819_db_user")
escaped_password = urllib.parse.quote_plus("admin819")

uri = f"mongodb+srv://dsh819_db_user:admin819@networksecurity.92qqjjg.mongodb.net/?appName=NetworkSecurity"
client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(f"Unable to connect to MongoDB: {e}")
