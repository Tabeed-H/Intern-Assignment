from pydantic import BaseModel
from uuid import UUID

"""
A pydantic model to define the structure of the response when creating or refreshing JWT tokens
"""
class TokenSchema(BaseModel):
    accessToken: str

"""
A pydantic model to parese and validate the payload of the incomming JWT token
"""
class TokenPayload(BaseModel):
    sub: UUID = None
    exp: int = None
    