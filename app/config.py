from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
  mongo_pass: str
  mongo_user: str
  mongo_cluster: str
  database: str
  client_origin: str
  access_token_expire_seconds: int
  algorithm: str
  secret_key: str

  model_config = SettingsConfigDict(env_file=".env")