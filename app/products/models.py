import uuid
from typing import Optional
from pydantic import BaseModel, Field

class ProductSchema(BaseModel):
  id: str = Field(default_factory=uuid.uuid4, alias="_id")
  product_name: str = Field(...)
  unit_price: int = Field(...)
  supplier_id: str = Field(...)
  quantity_in_stock: Optional[int] = None
  reorder_level: Optional[int] = None

  class Config:
    populate_by_name = True
    json_schema_extra = {
      "example": {
        "_id": "0afdb3a9-6ec5-4ac6-b435-e36cd325cae8",
        "product_name": "Test Product",
        "unit_price": 600,
        "supplier_id": "0afdb3a9-6ec5-4ac6-b435-e36cd325cae8",
        "quantity_in_stock": 8,
        "reorder_level": 2
      }
    }

class UpdateProductSchema(BaseModel):
  product_name: Optional[str] = None
  unit_price: Optional[int] = None
  supplier_id: Optional[str] = None
  quantity_in_stock: Optional[int] = None
  reorder_level: Optional[int] = None

  class Config:
    populate_by_name = True
    json_schema_extra = {
      "example": {
        "product_name": "Test Product",
        "unit_price": 600,
        "supplier_id": "0afdb3a9-6ec5-4ac6-b435-e36cd325cae8",
        "quantity_in_stock": 8,
        "reorder_level": 2
      }
    }