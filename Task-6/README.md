## 🌠 Task Tracker API

A simple and efficient FastAPI project to manage **Users** and their **Tasks** with built-in validation using **Pydantic**. This project provides RESTful endpoints to create users, assign tasks, and update task statuses.

---

### 📌 Features

✅ Create and retrieve users <br/>
✅ Create and manage tasks for users <br/>
✅ Update task status (with allowed values only) <br/>
✅ Get all tasks assigned to a user <br/>
✅ Pydantic validation for inputs (emails, due dates, status constraints)

---

### 📦 Requirements

* Python 3.9+
* FastAPI
* Uvicorn
* Pydantic

---

### 🧠 Models

#### 📄 User Models

* **UserCreate**

  * `username`: 3–20 characters
  * `email`: Valid email (EmailStr)

* **UserRead**

  * `id`: Auto-generated
  * `username`
  * `email`

#### 📝 Task Models

* **TaskCreate**

  * `title`
  * `description` *(optional)*
  * `due_date` *(must be today or later)*
  * `status` *(string)*
  * `user_id`

* **TaskUpdate**

  * `status`: Only `pending`, `in progress`, or `completed`

---

### 🛠️ Endpoints

#### 👤 Users

* `POST /users/` → Create user
* `GET /users/{user_id}` → Get user by ID

#### ✅ Tasks

* `POST /tasks/` → Create a new task
* `GET /tasks/{task_id}` → Get task by ID
* `PUT /tasks/{task_id}` → Update task status
* `GET /users/{user_id}/tasks` → Get all tasks for a user

---

### 📥 Installation

```bash
# 1. Clone the repository
git clone https://github.com/AyeshaNasirWebDeveloper/GIAIC-Q4-Learning/tree/main/Task-6
cd task-tracker-api

# 2. Create virtual environment
uv add venv
source .venv/Scripts/activate

# 3. Install dependencies
```bash
uv add fastapi[standard]
```

---

### ▶️ Run the API

```bash
fastapi run main.py
```

Visit the Swagger docs at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

### 🧪 Example Usage

#### Create User

```json
POST /users/
{
  "username": "ayesha",
  "email": "ayesha@gmail.com"
}
```

#### Create Task

```json
POST /tasks/
{
  "title": "Finish FastAPI Project",
  "description": "Complete by tonight",
  "due_date": "2025-05-13",
  "status": "pending",
  "user_id": 1
}
```

---

### ❤️ Contributing

Feel free to fork the project, make changes, and submit a pull request.

---
