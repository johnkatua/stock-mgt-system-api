from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import dotenv_values

config = dotenv_values()

app = FastAPI()

@app.get("/api/healthcheck")
def root():
  return {"message": "Welcome"}
