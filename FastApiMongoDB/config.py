import motor.motor_asyncio

# MONGODB_URL = 'mongodb://root:password123@localhost:27017'
# client=motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)

#connect to database
# database=client.Fastxpay

from pymongo import MongoClient

MONGO_CONNECTION_STRING = "mongodb://localhost:27017"
mongo_client = MongoClient(MONGO_CONNECTION_STRING)
mongo_db = mongo_client["Fastxpay"]
mongo_collection = mongo_db["users"]

# # Example: Insert a document into the "users" collection
# user_data = {"username": "john_doe", "email": "john@example.com"}
# result = mongo_collection.insert_one(user_data)
#
# print(f"Inserted document with ID: {result.inserted_id}")
