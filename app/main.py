from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import dotenv_values
from app.auth import auth_routes

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

app.include_router(auth_routes, tags=['Auth'], prefix='/api/auth')

@app.get("/api/healthcheck")
def root():
  return {"message": "Welcome"}
