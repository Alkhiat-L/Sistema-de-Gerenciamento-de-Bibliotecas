import datetime


class LibraryMediator:
    def __init__(self, database):
        self.database = database

    def book_search(self, user, mode, key):
        if not user.permissions['book_search']:
            return Exception
        books = []
        if mode == 'tittle':
            for book in self.database.books:
                if book.title == key:
                    books.append(book)
        if mode == 'author':
            for book in self.database.books:
                if book.author == key:
                    books.append(book)
        if mode == 'category':
            for book in self.database.books:
                if book.category == key:
                    books.append(book)
        if mode == 'available':
            for book in self.database.books:
                if book.available:
                    books.append(book)
        return books

    def book_borrow(self, user, book_id, days_borrowed):
        if user.permissions['book_borrow'] <= len(user.books):
            return Exception
        for lib_book in self.database.books:
            if book_id == lib_book.id and lib_book.disponible:
                lib_book.available = False
                lib_book.return_date = datetime.datetime.now() + datetime.timedelta(days=days_borrowed)
                return lib_book
        return Exception

    def book_return(self, user, book_id):
        if not user.permissions['book_return']:
            return Exception
        for lib_book in self.database.books:
            if book_id == lib_book.id and lib_book.borrowed_by == user.email:
                lib_book.available = True
                if lib_book.return_date > datetime.datetime.now():
                    return 0
                else:
                    return (lib_book.return_date - datetime.datetime.now()) * 0.5
        return Exception

    def user_search(self, user, mode, key):
        if not user.permissions['user_search']:
            return Exception
        users = []
        if mode == 'username':
            for lib_user in self.database.users:
                if key == lib_user.username:
                    users.append(lib_user)
        if mode == 'name':
            for lib_user in self.database.users:
                if key == lib_user.first_name + ' ' + lib_user.last_name:
                    users.append(lib_user)
        if mode == 'email':
            for lib_user in self.database.users:
                if key == lib_user.email:
                    users.append(lib_user)
        return users

    def book_add(self, user, book):
        if not user.permissions['book_add']:
            return Exception
        book.generate_id()
        self.database.books.append(book)
        return book

    def book_delete(self, user, book_id):
        #TODO: delete book function
        pass

