# ── BOOK CLASS ───────────────────────────────────────────────── 
# TODO: Define a class called Book
class Book:
    # TODO: Define __init__(self, title, author)
    # Set up three attributes:
    # self.title = title
    # self.author = author
    # self.is_borrowed = False  ← starts as not borrowed
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    # TODO: Define borrow(self)
    # If self.is_borrowed is already True → print that it's already borrowed
    # Otherwise → set self.is_borrowed = True and print a borrow message
    def borrow(self):
        if self.is_borrowed:
            print(f"Sorry, '{self.title}' is already borrowed.")
        else:
            self.is_borrowed = True
            print(f"You have successfully borrowed '{self.title}'.")

    # TODO: Define return_book(self)
    # If self.is_borrowed is False → print that it wasn't borrowed
    # Otherwise → set self.is_borrowed = False and print a return message
    def return_book(self):
        if not self.is_borrowed:
            print(f"Error: '{self.title}' was never borrowed.")
        else:
            self.is_borrowed = False
            print(f"Thank you for returning '{self.title}'.")

    # TODO: Define __str__(self)
    # Return a string like: "Title by Author [Available]"
    # or "Title by Author [Borrowed]"
    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"'{self.title}' by {self.author} [{status}]"


# ── LIBRARY ──────────────────────────────────────────────────── 
# TODO: Create at least 3 Book objects with different titles and authors
book1 = Book("Python Crash Course", "Eric Matthes")
book2 = Book("The Hobbit", "J.R.R. Tolkien")
book3 = Book("To Kill a Mockingbird", "Harper Lee")

print("=" * 42)
print(" 📚 LIBRARY SYSTEM")
print("=" * 42)

# TODO: Print each book (uses __str__ automatically)
print("\n--- Initial Catalog Status ---")
print(book1)
print(book2)
print(book3)

# TODO: Borrow some books using .borrow()
print("\n--- Borrowing Books ---")
book1.borrow()
book2.borrow()

# TODO: Try to borrow the same book twice to test the guard message
print("\n--- Testing Double Borrow Guard ---")
book1.borrow()

# TODO: Return a book using .return_book()
print("\n--- Returning Books ---")
book1.return_book()

# TODO: Try to return a book that was never borrowed to test that guard
print("\n--- Testing Unborrowed Return Guard ---")
book3.return_book()

# TODO: Print each book again to show updated status
print("\n--- Updated Catalog Status ---")
print(book1)
print(book2)
print(book3)


