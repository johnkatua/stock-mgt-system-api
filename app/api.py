import os
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from functools import lru_cache
from app.auth import auth_routes
from app.suppliers.routes import router as supplier_routes
from app.products.routes import router as product_routes
from app.auth.auth_bearer import JWTBearer
from app.config import Settings

client_origin = os.getenv("CLIENT_ORIGIN")
client_localhost = os.getenv("CLIENT_LOCALHOST")

app = FastAPI(redirect_slashes=False)

@lru_cache
def get_settings() -> Settings:
  """Load and cache settings from environment."""
  return Settings()

# Apply settings
settings = get_settings()

origins = [
  "*"
  # client_origin,
  # client_localhost
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_methods=["*"],
  allow_headers=["*"]
)

app.include_router(auth_routes.router, tags=['Auth'], prefix='/api/auth')
app.include_router(supplier_routes, tags=['Suppliers'], prefix='/api/suppliers')
app.include_router(product_routes, tags=['Products'], prefix='/api/products')

@app.get("/api/healthcheck", dependencies=[Depends(JWTBearer())])
def root():
  return {"message": f"Welcome"}
