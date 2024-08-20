from app.auth.auth_bearer import JWTBearer
from fastapi import APIRouter, Body, Depends

router = APIRouter()

@router.post(
    "/",
    response_description="Create a new product",
    dependencies=[Depends(JWTBearer())]
  )