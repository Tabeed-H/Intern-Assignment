from beanie import Document, Indexed, Link, before_event, Replace, Insert        # For MongoDB document mapping
from pydantic import Field, EmailStr       # For Data Validation
from uuid import UUID, uuid4                # For Generating UUIDS
from datetime import datetime               # For Working With Dates
from typing import Optional
from .userModel import User

class Todo(Document):
    todoId : UUID = Field(default_factory=uuid4, unique= True)
    status : bool = False
    title: Indexed(str)
    description: str
    createdAt: datetime = Field(default_factory=datetime.utcnow)
    updatedAt: datetime = Field(default_factory=datetime.utcnow)
    owner: Link[User]

    def __repr__(self) -> str:
        """
        This method provides a string representation of the object

        returns
        ------
        A string with the format '<Todo {self.title}'

        """
        return f"<Todo {self.title}>"
    
    def __str__(self) -> str:
        """
        This method provides a humann-readable string representaion of the object

        returns
        -------
        Email address of the user

        """
        return self.title
    
    def __hash__(self) -> int:
        """
        This method defines a custom hash value for instances of the class based on the todo title
        It allows instances to be used in hash-based collections like sets
        """
        return hash(self.title)
    
    def __eq__(self, other: object) -> bool:
        """
        This method defined the equality comparison between two instances of the class.

        returns
        ------
        'True' if the todo id are equal, 
        'False' otherwise

        """
        if isinstance(other, User):
            return self.todoId == other.todoId
        return False
    

    @before_event([Replace, Insert])
    def changeUpdateTime(self):
        self.updatedAt = datetime.utcnow()

    class Settings:
        name = "todos"
        user_revision = True
    