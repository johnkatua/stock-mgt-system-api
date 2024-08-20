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
      data=jsonable_encoder({
        "msg": "Product created successfully"
      })
    )
  except Exception as e:
    return JSONResponse(
      status_code=HttpStatus.CREATED,
      data=jsonable_encoder({
        "msg": str(e)
      })
    )
  
async def list_products() -> List[ProductSchema]:
  try:
    products = await list(Product.find(limit=100))
    return JSONResponse(
      status_code=HttpStatus.OK,
      data=products
    )
  except Exception as e:
    return JSONResponse(
      status_code=HttpStatus.CREATED,
      data=jsonable_encoder({
        "msg": str(e)
      })
    )