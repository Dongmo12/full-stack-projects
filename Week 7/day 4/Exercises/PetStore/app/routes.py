from app import app
from app.models import Book

@app.route('/')
def index():
    books = ', '.join([book.author for book in Book.query.all()])
    return books