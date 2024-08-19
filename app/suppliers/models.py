import uuid
from typing import Optional
from pydantic import BaseModel, Field

class SupplierSchema(BaseModel):
  id: str = Field(default_factory=uuid.uuid4, alias="_id")
  supplier_name: str = Field(...)
  contact_name: str = Field(...)
  phone: str = Field(...)
  address: Optional[str]

  class Config:
    populate_by_name = True
    json_schema_extra = {
      "example": {
        "_id": "0afdb3a9-6ec5-4ac6-b435-e36cd325cae8",
        "supplier_name": "Test Enterprises",
        "contact_name": "Test User",
        "phone": "0769654321",
        "address": "Tala, Kenya"
      }
    }

class UpdateSupplierSchema(BaseModel):
  supplier_name: Optional[str]
  contact_name: Optional[str]
  phone: Optional[str]
  address: Optional[str]

  class Config:
    json_schema_extra = {
      "example": {
        "supplier_name": "Test Enterprises",
        "contact_name": "Test User",
        "phone": "0769654321",
        "address": "Tala, Kenya"
      }
    }