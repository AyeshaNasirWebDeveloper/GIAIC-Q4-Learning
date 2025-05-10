# 📚 Book Library API

A simple and powerful **Book Library API** built with **FastAPI** that lets you perform CRUD operations on books, with validation for path and query parameters. Ideal for learning RESTful API development using Python and FastAPI.

---

## 🚀 Features

- 📖 Add a new book (title, author, price, description)
- 🧾 Retrieve all books or search using query parameters
- 🔍 Get a single book by ID with path validation
- ✏️ Update a book by ID
- ❌ Delete a book by ID
- ✅ Validation for query and path parameters
- 🧪 Interactive API Docs at `/docs` (Swagger UI)

---

## 🛠️ Built With

- **Python 3.11+**
- **FastAPI**
- **Pydantic**

---

## 📦 Installation & Running

```bash
# Clone the repo
git clone https://github.com/AyeshaNasirWebDeveloper/GIAIC-Q4-Learning/tree/main/Task-4
cd book-library-api

# Setup virtual environment
uv venv
source .venv/Scripts/activate

# Install FastAPI
uv add "fastapi[standard]"

# Run the development server
fastapi dev main.py
````

Then open: [http://localhost:8000/docs](http://localhost:8000/docs) for Swagger UI

---

## 🔗 API Endpoints

| Method | Endpoint           | Description          |
| ------ | ------------------ | -------------------- |
| GET    | `/books/`          | List all books       |
| GET    | `/books/{book_id}` | Get book by ID       |
| POST   | `/books/`          | Add a new book       |
| PUT    | `/books/{book_id}` | Update existing book |
| DELETE | `/books/{book_id}` | Delete a book        |

---

## 🧪 Validation Features

* `Path(...)` validation: ensures book ID is `int`, `ge=1`
* `Query(...)` parameters like `q`, `limit`, `skip` with:

  * `min_length`, `max_length`
  * `ge`, `le` for numeric values

---

## 🙌 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 🌐 Connect with Me

* LinkedIn: [Ayesha Nasir](https://www.linkedin.com/in/ayeshanasirwin/)
* GitHub: [Ayesha Nasir](https://github.com/AyeshaNasirWebDeveloper)

---

> “Code is like a book; you learn something new every time you read it.” 📘

```