from models import Book, User, Borrowing
from database import get_connection

class LibraryManager:
    def add_book(self, title, author, genre):
        book = Book(title, author, genre)
        book.save()

    def list_books(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        conn.close()

        if books:
            for book in books:
                status = "Available" if book[4] else "Borrowed"
                print(f"[{book[0]}] {book[1]} - {book[2]} ({book[3]}) - {status}")
        else:
            print("no book on library")

    def register_user(self, name, email):
        user = User(name, email)
        return user.save()

    def borrow_book(self, user_id, book_id):
        borrowing = Borrowing(user_id, book_id)
        borrowing.save()

    def return_book(self, borrow_id):
        Borrowing.return_book(borrow_id)

    def list_borrowings(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT borrowings.borrow_id, users.name, books.title, borrowings.borrow_date
            FROM borrowings
            JOIN users ON borrowings.user_id = users.user_id
            JOIN books ON borrowings.book_id = books.book_id
        """)
        borrowings = cursor.fetchall()
        conn.close()

        if borrowings:
            for b in borrowings:
                print(f"borrowed #{b[0]} - {b[1]} the '{b[2]}' at {b[3]}")
        else:
            print("empty reservations.")
