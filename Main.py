import json


class Book:
    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

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

    # SAVE
    def save_books(self):
        data = []

        for book in self.books:
            data.append({
                "book_id": book.book_id,
                "title": book.title,
                "author": book.author,
                "available": book.available
            })

        with open("books.json", "w") as file:
            json.dump(data, file, indent=4)

    # LOAD
    def load_books(self):
        try:
            with open("books.json", "r") as file:
                data = json.load(file)

            self.books = []

            for book in data:
                self.books.append(
                    Book(
                        book["book_id"],
                        book["title"],
                        book["author"],
                        book["available"]
                    )
                )

            print("Books loaded successfully.")

        except FileNotFoundError:
            print("No saved books found. Loading default books.")

            self.add_book(Book(1, "Harry Potter", "J.K. Rowling"))
            self.add_book(Book(2, "The Hobbit", "J.R.R. Tolkien"))
            self.add_book(Book(3, "Animal Farm", "George Orwell"))


def main():
    library = Library()

    # LOAD saved books when the program starts
    library.load_books()

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
            library.save_books()

        elif choice == "3":
            book_id = int(input("Enter book ID: "))
            library.return_book(book_id)
            library.save_books()

        elif choice == "4":
            library.save_books()
            print("Books saved successfully.")
            print("Thank you for using the School Library App!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
