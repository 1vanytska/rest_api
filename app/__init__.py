from flask import Flask
from app.views.book import book_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(book_bp, url_prefix="/books")
    return app
