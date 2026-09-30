class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        self.available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        print("\n--- Library Books ---")
        for book in self.books:
            status = "Available" if book.available else "Borrowed"
            print(f"{book.book_id}. {book.title} by {book.author} - {status}")

    def borrow_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.borrow():
                    print(f"You borrowed: {book.title}")
                else:
                    print("This book is already borrowed.")
                return
        print("Book not found.")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                book.return_book()
                print(f"You returned: {book.title}")
                return
        print("Book not found.")


def main():
    library = Library()

    library.add_book(Book(1, "Harry Potter", "J.K. Rowling"))
    library.add_book(Book(2, "The Hobbit", "J.R.R. Tolkien"))
    library.add_book(Book(3, "Animal Farm", "George Orwell"))

    while True:
        print("\n=== School Library App ===")
        print("1. Show books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            library.show_books()

        elif choice == "2":
            book_id = int(input("Enter book ID: "))
            library.borrow_book(book_id)

        elif choice == "3":
            book_id = int(input("Enter book ID: "))
            library.return_book(book_id)

        elif choice == "4":
            print("Thank you for using the School Library App!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
