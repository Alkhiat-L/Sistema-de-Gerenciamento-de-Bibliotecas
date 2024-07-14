import datetime
from entities.Book import Book
from entities.users.User import User

class Borrowing:
    def __init__(self, user: User, book: Book, borrow_date: datetime.datetime, return_date: datetime.datetime):
        self.user = user
        self.book = book
        self.borrow_date = borrow_date
        self.return_date = return_date
        self.book_returned_date = None
        self.status = 0     # 0 = "borrowed", 1 = "returned", 2 = "lateReturn"

    def return_book(self, book_returned_date: datetime.datetime):
        if book_returned_date < self.borrow_date:
            raise ValueError("Return date cannot be before borrow date.")
        elif book_returned_date <= self.return_date:
            self.status = 1
        elif book_returned_date > self.return_date:
            self.status = 2
        
        self.book_returned_date = book_returned_date