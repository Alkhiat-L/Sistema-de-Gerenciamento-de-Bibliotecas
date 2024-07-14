from library.LibraryMediator import LibraryMediator
from entities.users.User import User

class LibraryFacade:    #LibraryFacade
    def __init__(self, db):
        self.library = LibraryMediator(db)

    def book_search(self, username, password, mode, key):
        try:
            return self.library.book_search(username, password, mode, key)
        except Exception as e:
            print(f"Error in book search: {e}")
            return []

    def book_borrow(self, username, password, book_id, days_borrowed):
        try:
            self.library.book_borrow(username, password, book_id, days_borrowed)
            return True
        except Exception as e:
            print(f"Error in book borrowing: {e}")
            return False

    def book_return(self, username, password, book_id):
        try:
            self.library.book_return(username, password, book_id)
            return True
        except Exception as e:
            print(f"Error in book return: {e}")
            return False

    def user_search(self, username, password, mode, key):
        try:
            return self.library.user_search(username, password, mode, key)
        except Exception as e:
            print(f"Error in user search: {e}")
            return []

    def book_add(self, username, password, book):
        try:
            self.library.book_add(username, password, book)
            return True
        except Exception as e:
            print(f"Error in adding book: {e}")
            return False

    def book_delete(self, username, password, book_id):
        try:
            self.library.book_delete(username, password, book_id)
            return True
        except Exception as e:
            print(f"Error in deleting book: {e}")
            return False

    def user_register(self, username, password, first_name, last_name, new_username, email, new_password, user_type):
        try:
            self.library.user_register(username, password, first_name, last_name, new_username, email, new_password, user_type)
            return True
        except Exception as e:
            print(f"Error in register user: {e}")
            return False

