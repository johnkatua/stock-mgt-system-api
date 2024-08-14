from fastapi import status

class HttpStatus:
  CREATED = status.HTTP_201_CREATED
  UNAUTHORIZED = status.HTTP_401_UNAUTHORIZED
  NOT_FOUND = status.HTTP_404_NOT_FOUND
  BAD_REQUEST = status.HTTP_400_BAD_REQUEST