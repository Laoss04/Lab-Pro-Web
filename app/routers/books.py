from fastapi import APIRouter, Path, HTTPException, Query
from schemas.book import Book, books
from typing import Annotated
from schemas import review

books_router = APIRouter(prefix="/books", tags=["books"])

@books_router.get("/")
def get_all_books(
    sort: Annotated[bool, Query(description="Sort books by review")] = False
) -> list[Book]:
    if sort:
        return sorted(books.values(), key=lambda book: book.review)
    else:
        return list(books.values())

@books_router.get("/{id}")
def get_books_by_id(
    id: Annotated[int, Path(description="The ID of the book to get")]
) -> Book:
    try:
        books[id].review = review.review
        return "Review addedd successfully"
    except KeyError:
        raise HTTPException(status_code=404, detail="Book not found")

@books_router.post("/")
def add_book(book: Book):
    if book.id in books:
        raise HTTPException(status_code=403, detail="Book already exists")
    books[book.id] = book
    return "Book added successfully"

@books_router.put("/{id}")
def replace_book(
    id: Annotated[int, Path(description="The id of the book to replace")],
    book: Book
):
    if not id in books:
        raise HTTPException(status_code=404, detail="Book not found")
    books[id] = book
    return "Book replaced successfully"

@books_router.delete("/")
def delete_all_books():
    books.clear()
    return "All books deleted successfully"

@books_router.delete("/{id}")
def delete_book(
    id: Annotated[int, Path(description="The id of the book to delete")]
):
    if not id in books:
        raise HTTPException(status_code=404, detail="Book not found")
    del books[id]
    return "Book deleted successfully"