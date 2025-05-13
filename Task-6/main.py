from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, constr, validator
from datetime import date
from typing import Optional, List

app = FastAPI()

USERS: dict[int, dict] = {}
TASKS: dict[int, dict] = {}
user_id_counter = 1
task_id_counter = 1

# Pydantic Models
class UserCreate(BaseModel):
    username: constr(min_length=3, max_length=20)
    email: EmailStr

class UserRead(BaseModel):
    id: int
    username: str
    email: EmailStr

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str]
    due_date: date
    status: str
    user_id: int

    @validator('due_date')
    def validate_due_date(cls, v):
        if v < date.today():
            raise ValueError("Due date cannot be in the past")
        return v

class TaskCreate(BaseModel):
    title: str
    description: Optional[str]
    due_date: date
    status: str
    user_id: int

    @validator('due_date')
    def validate_due_date(cls, v):
        if v < date.today():
            raise ValueError("Due date cannot be in the past")
        return v

class TaskUpdate(BaseModel):
    status: str

    @validator("status")
    def status_validator(cls, v):
        allowed = ["pending", "in progress", "completed"]
        if v not in allowed:
            raise ValueError(f"Status must be one of: {', '.join(allowed)}")
        return v

# Routes of Users
@app.post("/users/", response_model=UserRead)
def create_user(user: UserCreate):
    global user_id_counter
    user_data = user.dict()
    user_data["id"] = user_id_counter
    USERS[user_id_counter] = user_data
    user_id_counter += 1
    return user_data

@app.get("/users/{user_id}", response_model=UserRead)
def get_user(user_id: int):
    user = USERS.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Routes of Tasks
@app.post("/tasks/", response_model=Task)
def create_task(task: TaskCreate):
    global task_id_counter
    if task.user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found")

    task_data = task.dict()
    task_data["id"] = task_id_counter
    TASKS[task_id_counter] = task_data
    task_id_counter += 1
    return task_data

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    task = TASKS.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task_status(task_id: int, task_update: TaskUpdate):
    task = TASKS.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task["status"] = task_update.status
    return task

@app.get("/users/{user_id}/tasks", response_model=List[Task])
def get_user_tasks(user_id: int):
    if user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found")
    return [task for task in TASKS.values() if task["user_id"] == user_id]
