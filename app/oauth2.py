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
expiry_time = config["ACCESS_TOKEN_EXPIRE_MINUTES"]

def generate_access_token(data: dict):
  to_encode = data.copy()
  expires_in = datetime.now() + timedelta(minutes=expiry_time)
  to_encode.update({"exp": expires_in})
  encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=hash_algorithm)
  return encoded_jwt

# def verify_token(token: str, credentials_exception):
#   try:
#     payload = jwt.decode(token, secret_key, algorithms=[hash_algorithm])
#     username: str = payload.get("sub")
#     if username is None:
#       raise credentials_exception
#     TokenData(username)
#   except JWTError:
#     raise credentials_exception

def decode_token(token: str) -> dict:
  try:
    decoded_token = jwt.decode(token, secret_key, algorithms=[hash_algorithm])
    return decoded_token if decoded_token["exp"] >= time.time() else None
  except:
    return {}

# def get_current_user(token: str = Depends(oauth2_scheme)):
#   credentials_exception = HTTPException(
#     status_code=HttpStatus.UNAUTHORIZED,
#     detail="Could not validate credentials",
#     headers={
#       "WWW-Authenticate": "Bearer"
#     }
#   )

#   return verify_token(token, credentials_exception)