from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from dotenv import dotenv_values
from app.auth import auth_routes
from app.auth.auth_bearer import JWTBearer
# from app.oauth2 import get_current_user

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

@app.get("/api/healthcheck", dependencies=[Depends(JWTBearer())])
def root():
  return {"message": f"Welcome"}
