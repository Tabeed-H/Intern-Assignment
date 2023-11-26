from fastapi import APIRouter, Depends
from app.schemas.todoSchema import TodoOut, TodoCreate, TodoUpdate
from app.models.userModel import User
from app.api.depencies.userDepencies import getCurrentUser
from app.services.todoService import TodoService
from app.models.todoModel import Todo
from typing import List
from uuid import UUID

todoRouter = APIRouter()        #  Create instance of Router

# Get All todos of the current logged in user
@todoRouter.get("/", summary="Get all todos of the user", response_model=List[TodoOut])
async def getCurrentUserTodo(user: User = Depends(getCurrentUser)):
    return await TodoService.listTodo(user)

# create a todo with the owner being the current logged in user
@todoRouter.post("/create", summary="Create Todo", response_model=Todo)
async def create(data: TodoCreate, user: User = Depends(getCurrentUser)):
    return await TodoService.createTodo(data, user)

# get a todo using its id
@todoRouter.get("/{todoId}", summary="Get todo by ID", response_model=TodoOut)
async def getTodoByID(todoId: UUID, user: User = Depends(getCurrentUser)):
    return await TodoService.getTodoUsingId(user, todoId=todoId)

# updat a todo using its id
@todoRouter.put("/{todoId}", summary="Update Todo By ID", response_model=TodoOut)
async def updateTodoByID(todoId: UUID,data: TodoUpdate, user: User = Depends(getCurrentUser)):
    return await TodoService.updateTodoUsingId(user, todoId=todoId, data=data)

# delete a todo using its id
@todoRouter.delete("/{todoId}", summary="Delete todo by ID", response_model=TodoOut)
async def deleteTodoById(todoId: UUID, user: User = Depends(getCurrentUser)):
    await TodoService.deleteTodoUsingId(user, todoId=todoId)
                   

