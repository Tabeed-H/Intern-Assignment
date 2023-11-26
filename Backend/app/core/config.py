from typing import List                         # For Defining List Types
from pydantic import BaseModel, AnyHttpUrl      # For Creating Settings Modal   'AnyHttpUrl for validating that a URL is an HTTP/HTTPS URL
from decouple import config                     # For Reading configurations from env varaibles


# Settings class inherits from 'BaseModel'
# Each attribute in the class represents a configuration setting with a default value
class Settings(BaseModel):
    API_STR: str = "/api/v1"
    JWT_SECRET: str = config("JWT_SECRET", cast=str)        # Fetched from env
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXP: int = 15
    BACKEND_CORS: List[AnyHttpUrl] = []
    PROJECT_NAME: str = "Intern-Todo"

    # Database
    MONOG_CONNECTION_URI_LOCAL: str = config("MONGO_CONNECTION_URI_LOCAL", cast= str)

    # To configure the behavior of the 'Settings' model
    # Here to make the attribute names case-sensitive
    class Config: 
        case_sensitive = True

# Creates an instance of the 'Settings' class to be used to access the configured settings throughout the application
settings = Settings()

