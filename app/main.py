from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import dotenv_values

config = dotenv_values(".env")

mongo_uri = config["MONGO_URI"]

app = FastAPI()

@app.get("/api/healthcheck")
def root():
  return {"message": "Welcome"}


client = MongoClient(mongo_uri)

try:
  client.admin.command('ping')
  print('pinged successfully')
except Exception as e:
  print(e)