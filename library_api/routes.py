from fastapi import APIRouter, HTTPException, status
from .schemas import BookSchema
from .storage import books

router = APIRouter()

@router.get("/books")
async def get_books():
    return books

@router.get("/books/{book_id}")
async def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@router.post("/books", status_code=status.HTTP_201_CREATED)
async def add_book(book: BookSchema):
    new_id = max(book["id"] for book in books) + 1 if books else 1
    new_book = {"id": new_id, **book.model_dump()}
    books.append(new_book)
    return new_book

@router.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")
