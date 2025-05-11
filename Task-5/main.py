from fastapi import FastAPI, Depends, Query, HTTPException, status
from typing import Annotated

app = FastAPI()

# 1. Basic Dependency
def fetch_mission():
    return {"mission": "I have to be the best AI model in the world."}

@app.get("/mission")
def read_mission(info: Annotated[dict, Depends(fetch_mission)]):
    return info


# 2. Dependency with Input Parameters
def personalized_mission(user: str):
    return {
        "mission": "I have to be the best AI model expert in the world.",
        "user": user
    }

@app.get("/user-mission")
def get_user_mission(data: Annotated[dict, Depends(personalized_mission)]):
    return data


# 3. Dependency with Query Parameters (Login Check)
def authenticate_user(username: str = Query(default=None), password: str = Query(default=None)):
    if username == "admin" and password == "admin123":
        return {"status": "Access Granted"}
    return {"status": "Access Denied"}

@app.get("/auth")
def login_status(auth_result: Annotated[dict, Depends(authenticate_user)]):
    return auth_result


# 4. Multiple Dependencies
def increment_by_one(n: int):
    return n + 1

def increment_by_two(n: int):
    return n + 2

@app.get("/calculate/{n}")
def compute_total(
    n: int,
    step_one: Annotated[int, Depends(increment_by_one)],
    step_two: Annotated[int, Depends(increment_by_two)]
):
    total = n + step_one + step_two
    return {"result": f"Total value is {total}"}


# 5. Using Class as Dependency
content_data = {
    "1": "Intro to GenAI",
    "2": "Basics of ML",
    "3": "Dive into Deep Learning"
}

user_records = {
    "8": "Nasir",
    "9": "Ayesha"
}

class FetchObject:
    def __init__(self, dataset):
        self.dataset = dataset

    def __call__(self, item_id: str):
        value = self.dataset.get(item_id)
        if not value:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Item with ID {item_id} not found."
            )
        return value

fetch_blog = FetchObject(content_data)
fetch_user = FetchObject(user_records)

@app.get("/content/{item_id}")
def get_content(title: Annotated[str, Depends(fetch_blog)]):
    return {"Content": title}

@app.get("/account/{item_id}")
def get_account(name: Annotated[str, Depends(fetch_user)]):
    return {"Username": name}
