from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from app.core.config import settings
from app.models.userModel import User
from jose import jwt
from app.schemas.authSchema import TokenPayload
from datetime import datetime
from pydantic import ValidationError
from app.services.userService import UserService
from typing import Annotated


# An instance of OAuth2PasswordBearer
# Used to extract and validate OAuth2 password bearer tokens
resuableAuth = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_STR}/auth/login",      # URL to request a token
    scheme_name="JWT"                               # Set authentication Scheme
)


"""
'getCurrentUser'
Used to retrieve the current user from a JWT token
Token is extreacted from the request using the 'resuableAuth' dependency
JWT token is decode and is validated against the JWT secret and algorithm sepcified in the settings

if the token is expired, HTTP exception is raised
if there are issuses with the decoding or validation, HTTP exception is reaised
if the token is valid the user is retrieved using the 'getUserByID' method from the 'UserServices'
if the user is not Found, HTTP excetion is raised
otherwise the user is returned
"""

async def getCurrentUser(token: Annotated[str, Depends(resuableAuth)]) -> User:
    try:
        print("hit")

        # decode token
        payload= jwt.decode(
            token, settings.JWT_SECRET, algorithms=[settings.ALGORITHM]
        )
        print("HITTT")
        print(payload)

        # compare with the token schema
        tokenData = TokenPayload(**payload)

        # check for expireation
        if datetime.fromtimestamp(tokenData.exp) < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail="Token Expired",
                headers={"WW-Authenticate": "Bearer"},
            )
  
    except(jwt.JWTError, ValidationError):
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail="Couldnot validate Token",
                headers={"WW-Authenticate": "Bearer"},
        )

    # Find user by ID
    user = await UserService.getUserByID(tokenData.sub)

    # if user not found
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find User"
        )
    
    # Return user
    return user
