from datetime import datetime, timedelta
from dotenv import dotenv_values
from jose import JWTError, jwt

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

def verify_token(token: str, credentials_exception):
  try:
    payload = jwt.decode(token, secret_key, algorithms=[hash_algorithm])
    username: str = payload.get("sub")
    if username is None:
      raise credentials_exception
    token_data = TokenData(username)
  except JWTError:
    raise credentials_exception