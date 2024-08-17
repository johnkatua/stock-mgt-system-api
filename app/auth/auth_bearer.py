from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.payload_util import HttpStatus

class JWTBearer(HTTPBearer):
  def __init__(self, auto_error: bool = True):
    super(JWTBearer, self).__init__(auto_error=auto_error)

  async def __call__(self, request: Request) -> HTTPAuthorizationCredentials | None:
    credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
    if credentials:
      if not credentials.scheme == "Bearer":
        raise HTTPException(status_code=HttpStatus.UNAUTHORIZED, detail="Invalid Authentication scheme.")
      if not self.verify_jwt(credentials.credentials):
        raise HTTPException(status_code=HttpStatus.UNAUTHORIZED, detail="Invalid Authentication scheme.")
      return credentials.credentials
    else:
      raise HTTPException(status_code=HttpStatus.UNAUTHORIZED, detail="Invalid Authorization code.")
    # return await super().__call__(request)