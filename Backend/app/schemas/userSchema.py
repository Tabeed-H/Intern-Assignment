from pydantic import BaseModel, EmailStr, Field
from uuid import UUID
from typing import Optional


"""
A pydantic model to validate incomming User data
"""
class UserAuth(BaseModel):
    email: EmailStr = Field(..., description= "User Email")
    username: str = Field(..., min_length=5, max_length=50, description="User Name")
    password : str = Field(..., min_length=5, description="User Password")


"""
A pydantic model to structure outgoing user data
"""
class UserOut(BaseModel):
    userId: UUID
    userName: str
    email: EmailStr
    firstName: Optional[str]
    lastName: Optional[str]
    disabled: Optional[str]