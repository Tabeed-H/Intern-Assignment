from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from datetime import datetime

"""
A pydantic model for the incomming data to be stored as todo
"""
class TodoCreate(BaseModel):
    title: str =  Field(..., title="Title", max_length=100, min_length=1)
    description: str = Field(..., title="Description", min_length=1)
    status: Optional[bool] = False

"""
A pydantic model for the incomming data used to update the todo
here the title, descroption and status are set optional as they can be the old todo as well and need no new changes
"""
class TodoUpdate(BaseModel):
    title: Optional[str] =  Field(..., title="Title", max_length=100, min_length=1)
    description: Optional[str] = Field(..., title="Description", min_length=1)
    status: Optional[bool] = False


"""
A pydantic model for outgoing todo
Structure a todo when sending as response
"""
class TodoOut(BaseModel):
    todoId: UUID
    status: bool
    title: str
    description: str
    createdAt: datetime
    updatedAt: datetime