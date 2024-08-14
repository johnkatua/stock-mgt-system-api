from pydantic import BaseModel, EmailStr, constr

class Register(BaseModel):
  name: str
  email: EmailStr
  password: str

class Login(BaseModel):
  email: EmailStr
  password: str

class Token(BaseModel):
  access_token: str
  token_type: str

class TokenData(BaseModel):
  username: str | None = None
