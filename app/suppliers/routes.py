from app.database import Supplier
from app.suppliers.models import SupplierSchema, UpdateSupplierSchema
from app.payload_util import HttpStatus
from app.auth.auth_bearer import JWTBearer
from fastapi import APIRouter, Body, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import List

router = APIRouter()

@router.post(
    '/', 
    response_description="Create a new supplier", 
    status_code=HttpStatus.CREATED, 
    response_model=SupplierSchema,
    dependencies=[Depends(JWTBearer())]
  )
async def create_supplier(payload: SupplierSchema = Body(...)):
  supplier = jsonable_encoder(payload)
  try:
    Supplier.insert_one(supplier)
    return JSONResponse(
      status_code=HttpStatus.CREATED,
      content=jsonable_encoder({
        "msg": "Supplier created successfully"
      })
    )
  except Exception as e:
    return JSONResponse(
      status_code=HttpStatus.SERVER_ERROR,
      content=jsonable_encoder({
        "msg": str(e)
      })
    )
  
@router.get(
    '/', 
    response_description="List all suppliers", 
    response_model=List[SupplierSchema],
    dependencies=[Depends(JWTBearer())]
  )
async def list_suppliers():
  try:
    suppliers = list(Supplier.find(limit=100))
    return JSONResponse(
      status_code=HttpStatus.OK,
      content=suppliers
    )
  except Exception as e:
    return JSONResponse(
      status_code=HttpStatus.SERVER_ERROR,
      content=jsonable_encoder({
        "msg": str(e)
      })
    )

@router.put(
    '/id', 
    response_description="Update a supplier", 
    response_model=UpdateSupplierSchema,
    dependencies=[Depends(JWTBearer())]
  )
async def update_supplier(id: str, payload: UpdateSupplierSchema = Body(...)):
  # Filter out None values from the input payload
  update_data = {k: v for k, v in payload.model_dump().items() if v is not None}

  if not update_data:
    return JSONResponse(
      status_code=HttpStatus.BAD_REQUEST,
      data=jsonable_encoder({
        "msg": "No valid fields provided for update"
      })
    )

  try:
    update_result = await Supplier.update_one({"_id": id}, {"$set": update_data})

    if update_result.modified_count == 0:
        return JSONResponse(
          status_code=HttpStatus.NOT_FOUND,
          data=jsonable_encoder({
            "msg": f"Supplier with ID {id} not found"
          })
        )
    
    updated_supplier = await Supplier.find_one({"_id": id})
    if updated_supplier:
      return JSONResponse(
          status_code=HttpStatus.OK,
          data=jsonable_encoder({
            "msg": f"Supplier with ID {id} updated successfully"
          })
        )
  except Exception as e:
    return JSONResponse(
      status_code=HttpStatus.SERVER_ERROR,
      data=jsonable_encoder({
        "msg": str(e)
      })
    )

@router.delete(
    "/{id}", 
    response_description="Delete a supplier",
    dependencies=[Depends(JWTBearer())]
  )
async def delete_supplier(id: str):
  try:
    delete_result = Supplier.delete_one({"_id": id})
    if delete_result.deleted_count == 1:
      return JSONResponse(
          status_code=HttpStatus.OK,
          content=jsonable_encoder({
            "msg": f"Supplier with ID {id} deleted successfully"
          })
        )
    
    return JSONResponse(
      status_code=HttpStatus.NOT_FOUND,
      content=jsonable_encoder({
        "msg": f"Supplier with ID {id} not found"
      })
    )
  except Exception as e:
    return JSONResponse(
      status_code=HttpStatus.SERVER_ERROR,
      content=jsonable_encoder({
        "msg": str(e)
      })
    )