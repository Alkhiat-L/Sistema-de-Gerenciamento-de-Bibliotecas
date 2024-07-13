from entities.Book import Book
from entities.BookCategory import BookCategory
from entities.Borrowing import Borrowing
from entities.users.User import User
from entities import BookAvailabilityNotifier


class DataBaseLocal(BookAvailabilityNotifier):
    def __init__(self):
        self.books = []
        self.book_categories = []
        self.borrowings = []
        self.maxDaysBorrowed = 7      #days

    def add_book(self, book: Book):
        self.books.append(book)
        self.notify('book_added', book)

    def remove_book(self, book: Book):
        if book in self.books:
            self.books.remove(book)
        self.notify('book_removed', book)

    def add_book_category(self, book_category: BookCategory):
        self.book_categories.append(book_category)

    def remove_book_category(self, book_category: BookCategory):
        if book_category in self.book_categories:
            self.book_categories.remove(book_category)

    def add_borrowing(self, borrowing: Borrowing):
        self.borrowings.append(borrowing)
        self.notify('book_borrowed', borrowing.book)

    def remove_borrowing(self, borrowing: Borrowing):
        if borrowing in self.borrowings:
            self.borrowings.remove(borrowing)
        self.notify('book_returned', borrowing.book)

    def get_max_days_borrowed(self):
        return self.maxDaysBorrowed
    
    def get_max_days_borrowed(self, new_time: int):
        self.maxDaysBorrowed = new_time

    def get_book_by_title(self, title: str) -> Book:
        for book in self.books:
            if book.title == title:
                return book
        return None
    
    def get_book_by_author(self, author: str) -> list:
        books_from_author = []
        for book in self.books:
            if book.author == author:
                books_from_author.append(book)
        return books_from_author

    def get_book_by_id(self, book_id: int) -> Book:
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    def get_books_by_category(self, category_name: str) -> list:
        books_in_category = []
        for book in self.books:
            if book.category == category_name:
                books_in_category.append(book)
        return books_in_category
    
    def get_books_avaiable(self) -> list:
        books_avaiable = []
        for book in self.books:
            if book.available == True:
                books_avaiable.append(book)
        return books_avaiable

    def get_borrowings_by_user(self, user: User) -> list:
        user_borrowings = []
        for borrowing in self.borrowings:
            if borrowing.user == user:
                user_borrowings.append(borrowing)
        return user_borrowings
