from app.schemas.userSchema import UserAuth         # Get user schema
from app.models.userModel import User               # get user model
from app.core.security import hashPassword          # get hashpassword function
from app.core.security import verifyPassword        # get verify hashed password function
from uuid import UUID
from typing import Optional


class UserService: 
    @staticmethod
    async def create(user: UserAuth):
        """
        parameters
        ----------
        user        type: UserAuth      user Schema
        
        Creates a new 'User' instance with the provided data
        Hashes the users password 
        saves the user to the db
        """
        userIN = User(
            userName= user.username,
            email = user.email,
            hashedPass= hashPassword(user.password),
        )

        await userIN.save()
        return userIN
    
    @staticmethod
    async def authenticate(email:str, password: str) -> Optional[User]:
        """
        parameters
        -----------
        email       type: Sting     user email
        password    type: string    user password plain text
        
        Method to authenticate the user
        retrives the user from te databased using 'getUserByEmail'
        if user doen't exists return NONE
        if the password verification fails return NONE
        if authenticated, return the user
        """
        user = await UserService.getUserByEmail(email=email)
        if not user:
            return None
        
        if not verifyPassword(password=password, hashedPassword=user.hashedPass):
            return None
        
        return user

    @staticmethod
    async def getUserByEmail(email: str) -> Optional[User]:
        """
        Takes an email as input and retrives a user from the data base based on the email
        """
        user = await User.find_one(User.email == email)
        return user
    
    @staticmethod
    async def getUserByID(id: UUID) -> Optional[User]:
        """
        Takes user ID as input and retrives a user from the data base based on the user ID
        """
        user = await User.find_one(User.userId == id)
        return user
