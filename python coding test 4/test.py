# ------------------------------------------------------------------------
# 1.  Book class      →  __init__ sets title, author, and is_borrowed = False
# 2.  borrow()        →  sets is_borrowed to True and prints a confirmation
# 3.  return_book()   →  sets is_borrowed to False and prints a confirmation
# 4.  3 Book objects  →  demonstrate both borrow() and return_book()
# 5.  self            →  used to access and update attributes inside methods



class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"you have borrowed '{self.title}' by {self.author}.")
        else:
            print(f"Sorry, '{self.title}' is already borrowed.")
            