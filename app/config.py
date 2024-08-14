from pydantic import BaseModel

class Settings(BaseModel):
  MONGO_URI: str

  class Config:
    env_file = './.env'

settings = Settings()