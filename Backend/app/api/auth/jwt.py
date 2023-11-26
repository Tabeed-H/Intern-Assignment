from fastapi import APIRouter, Depends, HTTPException, status           # Importing APIRouter to define router / Depends for handling Dependencies/ HTTPException for handling http exceptions/ status for HTTP status codes
from fastapi.security import OAuth2PasswordRequestForm                  # For Authentication
from app.core.security import createAccessToken                         # Method to create a JWT token
from app.services.userService import UserService                        # Import User Services
from app.schemas.authSchema import TokenSchema                          # Import Token Schema
from app.schemas.userSchema import UserOut                              # Import Schema for sending user data
from app.models.userModel import User                                   # Import User model
from app.api.depencies.userDepencies import getCurrentUser              # Import User Dependencies
from typing import Any

# Creating a new Router
authRouter = APIRouter()

"""
'login'
Used for Authentication using the OAuth2 password flow.

paramenter
----------
formData    type: OAuth2PasswordRequestForm     contains username ('emal') and password

calls the 'authenticate' method from the 'userService' to verity the users credentials
if authenticatin fails, it raises an 'HTTPExcaption' 
otherwise it create an access token using 'createAccessToken' method and returns the same as response
"""
@authRouter.post('/login', summary="Verify User", response_model=TokenSchema)
async def login(formData: OAuth2PasswordRequestForm = Depends()) -> Any:
    user = await UserService.authenticate(email= formData.username, password=formData.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect Email or Password"
        )
    
    # create Access Tokens
    return {
        "accessToken": createAccessToken(user.userId)
    }


# test route for testing jwt authentication
@authRouter.post('/test', summary="Test Token", response_model=UserOut)
async def test(user: User = Depends(getCurrentUser)):
    return user