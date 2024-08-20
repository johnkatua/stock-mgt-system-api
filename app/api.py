from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from dotenv import dotenv_values
from app.auth import auth_routes
from app.suppliers.routes import router as supplier_routes
from app.products.routes import router as product_routes
from app.auth.auth_bearer import JWTBearer

config = dotenv_values()

client_origin = config["CLIENT_ORIGIN"]

app = FastAPI()

origins = [
  client_origin
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)

app.include_router(auth_routes.router, tags=['Auth'], prefix='/api/auth')
app.include_router(supplier_routes, tags=['Suppliers'], prefix='/api/suppliers')
app.include_router(product_routes, tags=['Products'], prefix='/api/products')

@app.get("/api/healthcheck", dependencies=[Depends(JWTBearer())])
def root():
  return {"message": f"Welcome"}
