class Book:
    def __init__(self, book_id, title, author, publisher):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.publisher = publisher
        self.is_borrowed = False  # Book is available by default

    def display(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        print(
            f"ID: {self.book_id}, Title: {self.title}, "
            f"Author: {self.author}, Publisher: {self.publisher}, "
            f"Status: {status}"
        )


class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []

    def display(self):
        print(f"Patron ID: {self.patron_id}, Name: {self.name}")

        if self.borrowed_books:
            print("Borrowed Books:", ", ".join(self.borrowed_books))
        else:
            print("No books borrowed.")


class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}

    # Add a new book
    def add_book(self, book):
        self.books[book.book_id] = book
        print(f"Book '{book.title}' added successfully.")

    # Register a new patron
    def register_patron(self, patron):
        self.patrons[patron.patron_id] = patron
        print(f"Patron '{patron.name}' registered successfully.")

    # Borrow a book
    def borrow_book(self, patron_id, book_id):
        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        if book_id not in self.books:
            print("Book not found.")
            return

        patron = self.patrons[patron_id]
        book = self.books[book_id]

        if book.is_borrowed:
            print(f"Book '{book.title}' is already borrowed.")
        else:
            book.is_borrowed = True
            patron.borrowed_books.append(book.title)
            print(f"{patron.name} borrowed '{book.title}' successfully.")

    # Return a book
    def return_book(self, patron_id, book_id):
        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        if book_id not in self.books:
            print("Book not found.")
            return

        patron = self.patrons[patron_id]
        book = self.books[book_id]

        if book.title in patron.borrowed_books:
            patron.borrowed_books.remove(book.title)
            book.is_borrowed = False
            print(f"{patron.name} returned '{book.title}' successfully.")
        else:
            print(f"{patron.name} did not borrow '{book.title}'.")

    # Display all books
    def display_books(self):
        print("\n--- Library Books ---")
        for book in self.books.values():
            book.display()

    # Display all patrons
    def display_patrons(self):
        print("\n--- Registered Patrons ---")
        for patron in self.patrons.values():
            patron.display()


# ---------------- Main Program ----------------

library = Library()

# Add books
library.add_book(
    Book(101, "Python Programming", "Guido van Rossum", "Tech Publications")
)
library.add_book(
    Book(102, "Data Structures", "Mark Allen Weiss", "Academic Press")
)
library.add_book(
    Book(103, "Artificial Intelligence", "Stuart Russell", "Pearson")
)
library.add_book(
    Book(104, "Machine Learning", "Tom Mitchell", "McGraw Hill")
)

# Register patrons
library.register_patron(Patron(1, "Alice"))
library.register_patron(Patron(2, "Bob"))
library.register_patron(Patron(3, "Charlie"))

# Display all books
library.display_books()

# Borrow books
library.borrow_book(1, 101)
library.borrow_book(2, 102)
library.borrow_book(3, 104)

# Display updated books
library.display_books()

# Return a book
library.return_book(1, 101)

# Display final information
library.display_books()
library.display_patrons()
