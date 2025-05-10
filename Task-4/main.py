from fastapi import FastAPI, Path, Query, Body, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

books_db = []

# Pydantic model
class Book(BaseModel):
    title: str
    author: str
    description: Optional[str] = None
    price: float

# GET all books or search with query
@app.get("/books/", response_model=List[Book])
async def get_books(
    q: Optional[str] = Query(None, min_length=3),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, le=100)
):
    result = books_db[skip: skip + limit]
    if q:
        result = [book for book in result if q.lower() in book.title.lower()]
    return result

# GET a single book by ID
@app.get("/books/{book_id}", response_model=Book)
async def get_book(
    book_id: int = Path(..., ge=1, title="Book ID")
):
    if book_id > len(books_db) or book_id <= 0:
        raise HTTPException(status_code=404, detail="Book not found")
    return books_db[book_id - 1]

# POST endpoint
@app.post("/books/", response_model=Book)
async def create_book(book: Book):
    books_db.append(book)
    return book

# Update endpoint
@app.put("/books/{book_id}", response_model=Book)
async def update_book(
    book_id: int = Path(..., ge=1),
    book: Book = Body(...)
):
    if book_id > len(books_db) or book_id <= 0:
        raise HTTPException(status_code=404, detail="Book not found")
    books_db[book_id - 1] = book
    return book

# DELETE endpoint
@app.delete("/books/{book_id}")
async def delete_book(
    book_id: int = Path(..., ge=1)
):
    if book_id > len(books_db) or book_id <= 0:
        raise HTTPException(status_code=404, detail="Book not found")
    deleted_book = books_db.pop(book_id - 1)
    return {"message": "Book deleted successfully", "deleted_book": deleted_book}
