import datetime

from database.DataBaseLocal import DataBaseLocal
from entities.Borrowing import Borrowing
from handlers.HandlerSetup import HandlerSetup
from entities.users.StudentUserType import StudentUserType
from entities.users.TeacherUserType import TeacherUserType
from entities.users.LibrarianUserType import LibrarianUserType

class LibraryMediator:
    def __init__(self, database: DataBaseLocal):
        self.database = database    #localDataBase

    def get_user(self, username, password):
        user = False
        for u in self.database.users:
            if u.username == username:
                if u.password != password:
                    raise Exception('Wrong password')
                user = u
        if not user:
            raise Exception("User with this username does not exist")
        return user
    def book_search(self, username, password, mode, key):
        user = self.get_user(username, password)
        if not user.permissions['book_search']:
            raise Exception("Permission denied")
        books = []
        if mode == 'tittle':
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

    def book_borrow(self, username, password, book_id, days_borrowed):
        user = self.get_user(username, password)
        if not user.permissions['borrow']:
            raise Exception("Permission denied")

        handler_setup = HandlerSetup(self.database)
        handler_chain = handler_setup.setup_chain()

        request = {'user': user.id, 'book': book_id, 'days_borrowed': days_borrowed}
        result = handler_chain.handle(request)

        if result:
            book = self.database.get_book_by_id(book_id)
            book.available = False
            book.return_date = datetime.datetime.now() + datetime.timedelta(days=days_borrowed)
            borrowing = Borrowing(user, book, datetime.datetime.now(), book.return_date)
            self.database.add_borrowing(borrowing)
            return book
        else:
            raise Exception("Loan approval failed")

    def book_return(self, username, password, book_id):
        user = self.get_user(username, password)
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

    def user_search(self, username, password, mode, key):
        user = self.get_user(username, password)
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

    def book_add(self, username, password, book):
        user = self.get_user(username, password)
        if not user.permissions['add_book']:
            raise Exception("Permission denied")
        book.generate_id()
        self.database.add_book(book)
        return book

    def book_delete(self, username, password, book_id):
        user = self.get_user(username, password)
        if not user.permissions['remove_book']:
            raise Exception("Permission for remove book denied")
        
        book = self.database.get_book_by_id(book_id)
        if book:
            self.database.remove_book(book)
            return book
        raise Exception("Book not found")

    def user_register(self, username, password, first_name, last_name, new_username, email, new_password, user_type):
        user = self.get_user(username, password)
        if not user.permissions['register_user']:
            raise Exception("Permission for register user denied")
        for u in self.database.users:
            if u.username == new_username:
                raise Exception("Username already exists")
            if u.email == email:
                raise Exception("Email already exists")

        new_user = False

        if user_type == 'student':
            new_user = StudentUserType(first_name, last_name, new_username, email, new_password)
        if user_type == 'teacher':
            new_user = TeacherUserType(first_name, last_name, new_username, email, new_password)
        if user_type == 'librarian':
            new_user = LibrarianUserType(first_name, last_name, new_username, email, new_password)
        if new_user:
            self.database.add_user(new_user)
        return new_user
