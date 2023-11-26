from app.models.userModel import User
from app.models.todoModel import Todo
from app.schemas.todoSchema import TodoCreate, TodoUpdate
from typing import List
from uuid import UUID
class TodoService:
    @staticmethod
    async def listTodo(user: User) -> List[Todo]:
        """
        finds all the todos of the User
        """
        todos = await Todo.find(Todo.owner.id == user.id).to_list()
        return todos

    @staticmethod
    async def createTodo(data: TodoCreate, user: User) -> Todo:
        """
        Create a new todo with the owner being the current logged in user
        """
        todo = Todo(
            **data.dict(), owner = user
        )
        return await todo.insert()

    @staticmethod
    async def getTodoUsingId(user: User, todoId: UUID):
        """
        Get a todo using its ID and the owner being the current logged in user
        """
        todo = await Todo.find_one(Todo.todoId == todoId, Todo.owner.id == user.id)
        return todo
    
    @staticmethod
    async def updateTodoUsingId(user : User, todoId: UUID, data: TodoUpdate):
        """
        Update a todo using its ID
        """
        todo = await TodoService.getTodoUsingId(user, todoId=todoId)
        await todo.update({"$set" : data.dict(exclude_unset=True)})

        await todo.save()   # save the updated Todo
        return todo
    
    @staticmethod
    async def deleteTodoUsingId(user: User, todoId: UUID):
        """
        Deleted a todo using its ID
        """
        todo = await TodoService.getTodoUsingId(user, todoId=todoId)
        await todo.delete()

        return None