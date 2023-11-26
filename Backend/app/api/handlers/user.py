from fastapi import APIRouter, HTTPException, status        # Imports for Router/ HTTPException handling/ HTTP status codes
from app.schemas.userSchema import UserAuth, UserOut        # Imports for user Schema 
from app.services.userService import UserService            # Imports for user services

import pymongo      # Additional functionality over beanie

userRouter = APIRouter()        # Create instance of Router


"""
'createUser'

paramenter
----------
data    type: UserAuth (schema)

Calls the 'create' method from the 'userServices' to create a new user
Successful creation of user results in a response
Otherwise an HTTPExcaption is raised
"""
@userRouter.post('/create', summary="Create new User", response_model=UserOut)
async def createUser(data: UserAuth):
    try: 
        return await UserService.create(data)       # Async call to create function
    except pymongo.errors.DuplicateKeyError:

        # Raise exception if a user with the same usrname already exists
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST,
            detail="User with this email or username already exists"
        )
    