from fastapi import APIRouter, Request, Response
from payload_util import HttpStatus

router = APIRouter()

@router.post('/register', status_code=HttpStatus.CREATED)
async def create_user():
  pass