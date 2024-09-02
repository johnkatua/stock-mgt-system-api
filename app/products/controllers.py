from app.database import Product
from app.payload_util import HttpStatus
from app.products.models import ProductSchema, UpdateProductSchema
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import List

async def create_product(payload: ProductSchema):
  product = jsonable_encoder(payload)
  try:
    await Product.insert_one(product)
    return JSONResponse(
      status_code=HttpStatus.CREATED,
      content=jsonable_encoder({
        "msg": "Product created successfully"
      })
    )
  except Exception as e:
    return JSONResponse(
      status_code=HttpStatus.SERVER_ERROR,
      content=jsonable_encoder({
        "msg": str(e)
      })
    )
  
async def list_products() -> List[ProductSchema]:
  try:
    products = await list(Product.find(limit=100))
    return JSONResponse(
      status_code=HttpStatus.OK,
      content=products
    )
  except Exception as e:
    return JSONResponse(
      status_code=HttpStatus.SERVER_ERROR,
      content=jsonable_encoder({
        "msg": str(e)
      })
    )
  
async def delete_product(id: str):
  try:
    delete_result = await Product.delete_one({"id": id})
    if delete_result.deleted_count == 1:
      return JSONResponse(
        status_code=HttpStatus.OK,
        data=jsonable_encoder({
          "msg": f"Product with ID {id} deleted successfully"
        })
      )
    
    return JSONResponse(
      status_code=HttpStatus.NOT_FOUND,
      data=jsonable_encoder({
        "msg": f"Product with  ID {id} not found"
      })
    )
  except Exception as e:
    return JSONResponse(
      status_code=HttpStatus.SERVER_ERROR,
      data=jsonable_encoder({
        "msg": str(e)
      })
    )