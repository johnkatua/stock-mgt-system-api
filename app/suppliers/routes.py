from app.database import Supplier
from app.suppliers.models import SupplierSchema
from app.payload_util import HttpStatus
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import List

router = APIRouter()

@router.post('/', response_description="Create a new supplier", status_code=HttpStatus.CREATED, response_model=SupplierSchema)
async def create_supplier(payload: SupplierSchema = Body(...)):
  supplier = jsonable_encoder(payload)
  try:
    Supplier.insert_one(supplier)
    return JSONResponse(
      status_code=HttpStatus.CREATED,
      data=jsonable_encoder({
        "msg": "Supplier created successfully"
      })
    )
  except Exception as e:
    return JSONResponse(
      status_code=HttpStatus.SERVER_ERROR,
      data=jsonable_encoder({
        "msg": str(e)
      })
    )
  
@router.get('/', response_description="List all suppliers", response_model=List[SupplierSchema])
async def list_suppliers():
  try:
    suppliers = list(Supplier.find(limit=100))
    return JSONResponse(
      status_code=HttpStatus.OK,
      data=suppliers
    )
  except Exception as e:
    return JSONResponse(
      status_code=HttpStatus.SERVER_ERROR,
      data=jsonable_encoder({
        "msg": str(e)
      })
    )
