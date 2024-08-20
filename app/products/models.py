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

class UpdateProductSchema(BaseModel):
  product_name: Optional[str] = None
  unit_price: Optional[int] = None
  supplier_id: Optional[str] = None
  quantity_in_stock: Optional[int] = None
  reorder_level: Optional[int] = None