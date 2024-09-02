from app.auth.auth_bearer import JWTBearer
from app.products.models import ProductSchema, UpdateProductSchema
from app.products.controllers import create_product, list_products, delete_product
from fastapi import APIRouter, Body, Depends
from typing import List

router = APIRouter()

@router.post(
    "/",
    response_description="Create a new product",
    dependencies=[Depends(JWTBearer())]
  )
async def create_product_route(payload: ProductSchema = Body(...)):
  await create_product(payload)


@router.get(
    "/",
    response_model=List[ProductSchema],
    response_description="List all products",
    dependencies=[Depends(JWTBearer())]
  )
async def list_products_route():
  return await list_products()

@router.delete(
    "/{id}",
    response_description="Delete a product",
    dependencies=[Depends(JWTBearer())]
  )
async def delete_product_route(id: str):
  await delete_product(id)