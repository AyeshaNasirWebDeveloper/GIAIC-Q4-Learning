# 🤖 DACA Chatbot API

Welcome to the **DACA Chatbot API** – a FastAPI-powered conversational backend built with a modular, agentic workflow in mind.

## 🚀 Features

- 📬 Accepts rich user messages with metadata (timestamp, session ID, tags)
- 💬 Intelligent chatbot replies via `/talk/` endpoint
- 📎 Pydantic models for structured and scalable data handling
- 🔍 Auto-generated docs at `/docs` (Swagger) and `/redoc`

## 📦 Tech Stack

- **FastAPI**
- **Pydantic**
- **Uvicorn**
- **Python 3.11+**

## ▶ Quickstart

```bash
fastapi dev main.py

PYDANTIC