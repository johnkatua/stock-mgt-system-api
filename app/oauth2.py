import time
from app.auth.models import TokenData
from datetime import datetime, timedelta
from dotenv import dotenv_values
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from app.payload_util import HttpStatus

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

config = dotenv_values("./.env")

secret_key = config["SECRET_KEY"]
hash_algorithm = config["ALGORITHM"]
expiry_time = config["ACCESS_TOKEN_EXPIRE_SECONDS"]

def generate_access_token(data: dict):
  to_encode = data.copy()
  expires_in = time.time() + float(expiry_time)
  to_encode.update({"exp": expires_in})
  encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=hash_algorithm)
  return encoded_jwt

def decode_token(token: str) -> dict:
  try:
    decoded_token = jwt.decode(token, secret_key, algorithms=[hash_algorithm])
    return decoded_token if decoded_token["exp"] >= time.time() else None
  except:
    return {}