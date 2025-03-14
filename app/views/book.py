from flask import Blueprint, jsonify, request
from ..schemas.book_schema import BookSchema
from ..storage.book_storage import books
from ..models.book_model import Book

book_schema = BookSchema()
books_schema = BookSchema(many=True)

book_bp = Blueprint('book_bp', __name__)

@book_bp.route('/', methods=['GET'])
def get_books():
    return jsonify({"books": books_schema.dump(books)})

@book_bp.route('/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(book_schema.dump(book))

@book_bp.route('/', methods=['POST'])
def add_book():
    data = request.get_json()
    
    errors = book_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    book = Book(data["title"], data["author"])
    books.append(book)

    return jsonify(book_schema.dump(book.to_dict())), 201

@book_bp.route('/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    
    if book is None:
        return jsonify({"message": "Book not found"}), 404
    
    books.remove(book)
    return jsonify({"message": f"Book with ID {book_id} has been deleted"}), 200

