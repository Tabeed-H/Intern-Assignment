from passlib.context import CryptContext        # Import for bcrypt
from datetime import datetime, timedelta        # Handling date
from app.core.config import settings            # IMport Settings
from jose import jwt                            # JWT 
from typing import Union, Any               

# Creating an instance of cryptContext
# Configurating to use 'bcrypt' hashing 
# deprecated set to 'auto' to use the latest available version of the hash
passwordContext = CryptContext(schemes=['bcrypt'], deprecated= "auto")      


"""
'hashPassword'

parameters
----------
password    type: string    plain password

function takes plain-text password as input and returns its hashed version
"""
def hashPassword(password: str) -> str:
    return passwordContext.hash(password)


"""
'verifyPassword'

parameters
----------
password        type: string    plain text password
hashedPassword  type: String    user stored hashed password

function takes palin text password and its hashed version as input and returns 'True' if the password matched the hashed version, otherwise 'False'
"""
def verifyPassword(password: str, hashedPassword: str) -> bool:
    return passwordContext.verify(password, hashedPassword)


"""
'createAccessToken'

parameters
-----------
subject     type: String    userID
expires     type: interger  expiration time of token if specified   default: None

The function creates a dictionary with the expiration ('exp') and subject ('sub') encodes the JWT and returns the encoded JWT token
"""
def createAccessToken(subject: Union[str, Any], expires: int = None) -> str:
    # if expire is given
    if expires is not None:
        expires = datetime.utcnow() + expires
    else:
        # if expire time is not given get from settings
        expires = datetime.utcnow() + timedelta(minutes = settings.ACCESS_TOKEN_EXP)

    encode = {"exp": expires, "sub": str(subject)}  # dictionary to encode
    encodedJwt = jwt.encode(encode, settings.JWT_SECRET, settings.ALGORITHM)    # Ecnode message
    return encodedJwt   # Returen token