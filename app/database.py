from dotenv import dotenv_values
from pymongo.mongo_client import MongoClient
import os

config = dotenv_values("./.env")

mongo_uri = os.getenv("MONGO_URI")
database = os.getenv("DATABASE")

client = MongoClient(mongo_uri)
db = client[database]

User = db.users
Supplier = db.suppliers
Product = db.products