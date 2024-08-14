from database import User
from fastapi import APIRouter, HTTPException
from models import Register, Login
from payload_util import HttpStatus
from utils import hash_password, verify_password

router = APIRouter()

@router.post('/register', status_code=HttpStatus.CREATED)
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
      detail=f"No user with the email of {payload.email}"
    )
  
  if not verify_password(payload.password, user["password"]):
    raise HTTPException(
      status_code=HttpStatus.BAD_REQUEST,
      detail="Incorrect Email or Password"
    )