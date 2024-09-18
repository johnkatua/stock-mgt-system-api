import time
from dotenv import dotenv_values
import os
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

config = dotenv_values("./.env")

secret_key =  os.getenv("SECRET_KEY") #config["SECRET_KEY"]
# hash_algorithm = config["ALGORITHM"]
hash_algorithm = os.getenv("ALGORITHM")
# expiry_time = config["ACCESS_TOKEN_EXPIRE_SECONDS"]
expiry_time = os.getenv("ACCESS_TOKEN_EXPIRE_SECONDS")

def generate_access_token(data: dict):
  to_encode = data.copy()
  expires_in = time.time() + float(expiry_time)
  to_encode.update({"exp": expires_in})
  encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=hash_algorithm)
  return encoded_jwt

def get_token_payload(token: str):
  try:
    payload = jwt.decode(token, secret_key, algorithms=hash_algorithm)
  except JWTError:
    return None
  return payload

def decode_token(token: str) -> dict:
  try:
    decoded_token = jwt.decode(token, secret_key, algorithms=[hash_algorithm])
    return decoded_token if decoded_token["exp"] >= time.time() else None
  except:
    return {}