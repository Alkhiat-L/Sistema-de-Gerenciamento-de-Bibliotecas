import datetime

from externalcatalog import ExternalCatalog
from library.Library import Library  # Import LibraryFacade instead of LibraryMediator

class ExternalCatalogAdapter(ExternalCatalog):
    def __init__(self, library_facade: Library):
        self.library_facade = library_facade

    def search_books(self, mode, key):
        if mode == 'title':
            return self.library_facade.book_search(None, 'title', key)
        elif mode == 'author':
            return self.library_facade.book_search(None, 'author', key)
        elif mode == 'category':
            return self.search_books_by_category(key)
        elif mode == 'available':
            return self.search_available_books()
        elif mode == 'id':
            return self.search_book_by_id(key)
        else:
            raise Exception("Invalid search mode")

    def borrow_book(self, user_id, book_id, days_borrowed):
        user = self.get_user_by_id(user_id)
        if not user:
            raise Exception(f"User with ID {user_id} not found")

        return self.library_facade.book_borrow(user, book_id, days_borrowed)

    def return_book(self, user_id, book_id):
        user = self.get_user_by_id(user_id)
        if not user:
            raise Exception(f"User with ID {user_id} not found")

        return self.library_facade.book_return(user, book_id)

    def search_users(self, mode, key):
        if mode == 'username':
            return self.library_facade.user_search(None, 'username', key)
        elif mode == 'name':
            return self.library_facade.user_search(None, 'name', key)
        elif mode == 'email':
            return self.library_facade.user_search(None, 'email', key)
        elif mode == 'id':
            return self.get_user_by_id(key)
        else:
            raise Exception("Invalid search mode")

    def search_books_by_category(self, category):
        books = []
        for book_category in self.library_facade.library.database.book_categories:
            if book_category.belongs_to_category(category):
                books.extend(book_category.get_books())
        return books

    def search_available_books(self):
        return self.library_facade.library.database.get_books_available()

    def search_book_by_id(self, book_id):
        book = self.library_facade.library.database.get_book_by_id(book_id)
        if book:
            return [book]
        else:
            return []

    def get_user_by_id(self, user_id):
        return self.library_facade.library.database.get_user_by_id(user_id)
