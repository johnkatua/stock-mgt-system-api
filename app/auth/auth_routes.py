from app.database import User
from app.auth.models import Register, Login, Token
from app.oauth2 import generate_access_token, get_token_payload
from app.payload_util import HttpStatus
from app.utils import hash_password, verify_password
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.post("/register", status_code=HttpStatus.CREATED)
async def create_user(payload: Register):
  hashed_pwd = hash_password(payload.password)
  user = dict(payload)
  user["password"] = hashed_pwd
  User.insert_one(user)
  return {
    "status_code": 200,
    "detail": "User created successfully"
  }

@router.post('/login', status_code=HttpStatus.CREATED)
async def login(payload: Login):
  user = User.find_one({"email": payload.email.lower()})
  if not user:
    raise HTTPException(
      status_code=HttpStatus.NOT_FOUND,
      detail=f"No user with the email of {payload.email} found"
    )
  
  if not verify_password(payload.password, user["password"]):
    raise HTTPException(
      status_code=HttpStatus.BAD_REQUEST,
      detail="Incorrect Email or Password"
    )
  
  access_token = generate_access_token(
    data={"user": user["email"]}
  )

  decoded_token = get_token_payload(access_token)

  return {
    "access_token": access_token, 
    "token_type": "bearer", 
    "expires_in": decoded_token['exp'],
    "user": decoded_token['user']
  }

@router.post("/refresh-token", status_code=HttpStatus.CREATED)
async def refresh_token(token: Token):
  decoded_token = get_token_payload(token.access_token)
  user_email = None
  if decoded_token is not None:
    user_email = decoded_token.get('user', None)
  if not user_email:
    raise HTTPException(
      status_code=HttpStatus.UNAUTHORIZED,
      detail="Invalid access token",
      headers={
        "WWW-Authenticate": "Bearer"
      }
    )
  
  user = User.find_one({"email": user_email})

  if not user:
    raise HTTPException(
      status_code=HttpStatus.UNAUTHORIZED,
      detail="Invalid access token",
      headers={
        "WWW-Authenticate": "Bearer"
      }
    )
  
  access_token = generate_access_token(
    data={"user": user["email"]}
  )

  decoded_token = get_token_payload(access_token)

  return {
    "access_token": access_token, 
    "token_type": "bearer", 
    "expires_in": decoded_token['exp'],
    "user": decoded_token['user']
  }
