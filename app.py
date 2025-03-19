from library_manager import LibraryManager

def main():
    library = LibraryManager()

    while True:
        print("\n1. Show books\n2. Create account\n3. Borrow book\n4. show resevertions\n5. Return book\n6. Exit")
        choice = input("Choose action: ")

        if choice == "1":
            library.list_books()
        elif choice == "2":
            name = input("Username: ")
            email = input("Email: ")
            library.register_user(name, email)
        elif choice == "3":
            user_id = int(input("user ID: "))
            book_id = int(input("book ID: "))
            library.borrow_book(user_id, book_id)
        elif choice == "4":
            library.list_borrowings()
        elif choice == "5":
            borrow_id = int(input("Reservation ID: "))
            library.return_book(borrow_id)
        elif choice == "6":
            print("Exit...")
            break
        else:
            print("Unvalid option")

if __name__ == "__main__":
    main()
