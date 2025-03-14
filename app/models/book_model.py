from ..storage.book_storage import books

class Book:
    def __init__(self, title, author, book_id=None):
        if book_id is None:
            self.id = Book.generate_id()
        else:
            self.id = book_id
        self.title = title
        self.author = author

    @staticmethod
    def generate_id():
        return max([book["id"] for book in books], default=0) + 1

    def to_dict(self):
        return {"id": self.id, "title": self.title, "author": self.author}
