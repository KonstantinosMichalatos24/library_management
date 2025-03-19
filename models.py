from database import get_connection

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (title, author, genre, available) VALUES (%s, %s, %s, TRUE)",
                       (self.title, self.author, self.genre))
        conn.commit()
        conn.close()

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (self.name, self.email))
        conn.commit()
        user_id = cursor.lastrowid
        conn.close()
        return user_id

class Borrowing:
    def __init__(self, user_id, book_id):
        self.user_id = user_id
        self.book_id = book_id

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT available FROM books WHERE book_id = %s", (self.book_id,))
        book = cursor.fetchone()
        if not book or not book[0]:
            print("book isnt avalaible.")
            conn.close()
            return

        cursor.execute("INSERT INTO borrowings (user_id, book_id, borrow_date) VALUES (%s, %s, NOW())",
                       (self.user_id, self.book_id))
        cursor.execute("UPDATE books SET available = FALSE WHERE book_id = %s", (self.book_id,))
        conn.commit()
        conn.close()
        print("book borrowed succesfully.")

    @staticmethod
    def return_book(borrow_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT book_id FROM borrowings WHERE borrow_id = %s", (borrow_id,))
        book = cursor.fetchone()
        if book:
            cursor.execute("DELETE FROM borrowings WHERE borrow_id = %s", (borrow_id,))
            cursor.execute("UPDATE books SET available = TRUE WHERE book_id = %s", (book[0],))
            conn.commit()
            print("book returned.")
        else:
            print("book resservation not found.")
        conn.close()
