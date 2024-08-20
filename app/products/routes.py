from app.auth.auth_bearer import JWTBearer
from app.products.models import ProductSchema, UpdateProductSchema
from app.products.controllers import create_product, list_products
from fastapi import APIRouter, Body, Depends

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
  response_description="List all products",
  dependencies=[Depends(JWTBearer)]
)
async def list_products_route():
  await list_products()

