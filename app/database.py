from dotenv import dotenv_values
from pymongo.mongo_client import MongoClient

config = dotenv_values("./.env")

mongo_uri = config["MONGO_URI"]
database = config["DATABASE"]

client = MongoClient(mongo_uri)
db = client[database]

User = db.users
Supplier = db.suppliers
Product = db.products