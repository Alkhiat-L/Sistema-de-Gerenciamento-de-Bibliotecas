from Entities.Book import Book
from Entities.BookCategory import BookCategory
from Entities.Borrowing import Borrowing
from Entities.users.User import User

class DataBaseLocal:
    def __init__(self):
        self.books = []
        self.book_categories = []
        self.borrowings = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, book: Book):
        if book in self.books:
            self.books.remove(book)

    def add_book_category(self, book_category: BookCategory):
        self.book_categories.append(book_category)

    def remove_book_category(self, book_category: BookCategory):
        if book_category in self.book_categories:
            self.book_categories.remove(book_category)

    def add_borrowing(self, borrowing: Borrowing):
        self.borrowings.append(borrowing)

    def remove_borrowing(self, borrowing: Borrowing):
        if borrowing in self.borrowings:
            self.borrowings.remove(borrowing)

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

    def get_borrowings_by_user(self, user: User) -> list:
        user_borrowings = []
        for borrowing in self.borrowings:
            if borrowing.user == user:
                user_borrowings.append(borrowing)
        return user_borrowings