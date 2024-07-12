import datetime

from DataBase.DataBaseLocal import DataBaseLocal
from Entities.Borrowing import Borrowing

class LibraryMediator:
    def __init__(self, database: DataBaseLocal):
        self.database = database    #localDataBase

    def book_search(self, user, mode, key):
        if not user.permissions['book_search']:
            raise Exception("Permission denied")
        books = []
        if mode == 'title':
            for book in self.database.books:
                if book.title == key:
                    books.append(book)
        elif mode == 'author':
            for book in self.database.books:
                if book.author == key:
                    books.append(book)
        elif mode == 'category':
            for category in self.database.book_categories:
                if category.belongs_to_category(key):
                    books.append(category.get_books())
        elif mode == 'available':
            for book in self.database.books:
                if book.available:
                    books.append(book)
        elif mode == 'id':
            for book in self.database.books:
                if book.id == key:
                    books.append(book)
        return books

    def book_borrow(self, user, book_id, days_borrowed):
        if not user.permissions['borrow']:
            raise Exception("Permission denied")
        if user.permissions['borrow'] <= len(user.books):
            raise Exception("Borrow limit exceeded")
        
        book = self.database.get_book_by_id(book_id)
        if book and book.available:
            book.available = False
            book.return_date = datetime.datetime.now() + datetime.timedelta(days=days_borrowed)
            borrowing = Borrowing(user, book, datetime.datetime.now(), book.return_date)
            self.database.add_borrowing(borrowing)
            return book
        
        raise Exception("Book not available")

    def book_return(self, user, book_id):
        if not user.permissions['return']:
            raise Exception("Permission denied")
        for borrowing in self.database.borrowings:
            if borrowing.book.id == book_id and borrowing.user == user:
                borrowing.return_book(datetime.datetime.now())
                if borrowing.status == 2:
                    return (datetime.datetime.now() - borrowing.return_date).days * 0.5
                else:
                    return 0
        raise Exception("Book not borrowed by user")

    def user_search(self, user, mode, key):
        if not user.permissions['user_search']:
            raise Exception("Permission denied")
        users = []
        if mode == 'username':
            for lib_user in self.database.users:
                if key == lib_user.username:
                    users.append(lib_user)
        elif mode == 'name':
            for lib_user in self.database.users:
                if key == lib_user.first_name + ' ' + lib_user.last_name:
                    users.append(lib_user)
        elif mode == 'email':
            for lib_user in self.database.users:
                if key == lib_user.email:
                    users.append(lib_user)
        elif mode == 'id':
            for lib_user in self.database.users:
                if key == lib_user.id:
                    users.append(lib_user)
        return users

    def book_add(self, user, book):
        if not user.permissions['add_book']:
            raise Exception("Permission denied")
        book.generate_id()
        self.database.add_book(book)
        return book

    def book_delete(self, user, book_id):
        if not user.permissions['remove_book']:
            raise Exception("Permission for remove book denied")
        
        book = self.database.get_book_by_id(book_id)
        if book:
            self.database.remove_book(book)
            return book
        raise Exception("Book not found")

