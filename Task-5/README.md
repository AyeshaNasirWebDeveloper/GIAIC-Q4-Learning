# :airplane: FastAPI Dependency Injection

This project demonstrates the use of **Dependency Injection** in FastAPI through simple and practical examples. It showcases how to write clean, reusable, and testable API logic using built-in `Depends` and custom dependencies including class-based dependencies.

---

## 📚 Project Overview

FastAPI makes it easy to inject dependencies for shared logic like authentication, database access, validation, and more. This project contains 5 example use-cases:

### ✅ Features Covered

1. **Simple Dependency**  
   A basic function dependency used in an endpoint.

2. **Dependency with Parameters**  
   Injecting values like usernames and using them dynamically in your logic.

3. **Authentication with Query Parameters**  
   Checking credentials passed as query parameters using a dependency.

4. **Multiple Dependencies in a Single Endpoint**  
   Demonstrates how to run multiple dependency functions together.

5. **Class-based Dependency**  
   Simulating a mini-database fetch with error handling using custom classes.

---

## 🛠️ Technologies Used

- Python 3.11+
- FastAPI
- Uvicorn (for local development server)

---

## 🚦 How to Run

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/AyeshaNasirWebDeveloper/GIAIC-Q4-Learning/tree/main/Task-5
   cd fastapi-dependency-injection
````

2. **Create a Virtual Environment:**

   ```bash
   uv venv
   source .venv/Scripts/activate
   ```

3. **Install Dependencies:**

   ```bash
   uv add "fastapi[standard]"
   ```

4. **Run the API:**

   ```bash
   fastapi run main.py
   ```

---

## 📌 API Endpoints

| Endpoint                      | Description                             |
| ----------------------------- | --------------------------------------- |
| `/mission`                    | Returns a basic mission object          |
| `/user-mission`               | Accepts a username and returns message  |
| `/auth?username=x&password=y` | Simple login checker                    |
| `/calculate/{n}`              | Adds multiple values using dependencies |
| `/content/{item_id}`          | Fetches blog/content info from dict     |
| `/account/{item_id}`          | Fetches user info from dict             |

---

## ✨ Author

**Ayesha Nasir**
📧 [my email](ayeshanasir07000@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/ayeshanasirwin/) 
🔗 [GitHub](https://github.com/AyeshaNasirWebDeveloper)

---
