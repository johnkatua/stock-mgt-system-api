from dotenv import dotenv_values
from pymongo.mongo_client import MongoClient
import os

config = dotenv_values("./.env")
# MONGO_URI="mongodb+srv://johnkatua:sIlzKWnBRkxOWAPq@cluster0.b4ovhgj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

MONGO_PASS = os.getenv("MONGO_PASS")
MONGO_USER = os.getenv("MONGO_USER")
MONGO_CLUSTER = os.getenv("MONGO_CLUSTER")
mongo_uri = f"mongodb+srv://{MONGO_USER}:{MONGO_PASS}@{MONGO_CLUSTER}/?retryWrites=true&w=majority&appName=Cluster0"
database = os.getenv("DATABASE")

client = MongoClient(mongo_uri)
db = client[database]

User = db.users
Supplier = db.suppliers
Product = db.products