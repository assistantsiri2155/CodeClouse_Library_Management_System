class Book:
    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies
        
class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        
    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                
    def display_books(self):
        for book in self.books:
            print(f"Title: {book.title}\nAuthor: {book.author}\nISBN: {book.isbn}\nCopies available: {book.copies}\n")
                
    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.copies > 0:
                    book.copies -= 1
                    print("Book borrowed successfully!")
                else:
                    print("Sorry, no copies available!")
                return
        print("Sorry, book not found!")
        
    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                book.copies += 1
                print("Book returned successfully!")
                return
        print("Sorry, book not found!")
        

library = Library()

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-3-16-148410-0", 2)
book2 = Book("To Kill a Mockingbird", "Harper Lee", "978-0-446-31078-0", 1)
book3 = Book("1984", "George Orwell", "978-0-452-28423-4", 3)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.display_books()

library.borrow_book("978-3-16-148410-0")
library.borrow_book("978-3-16-148410-0")
library.borrow_book("978-0-446-31078-0")
library.borrow_book("978-0-452-28423-4")

library.return_book("978-0-446-31078-0")

library.display_books()
