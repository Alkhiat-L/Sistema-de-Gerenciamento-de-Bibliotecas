from library.LibraryMediator import LibraryMediator
from entities.users.User import User

class LibraryFacade:    #LibraryFacade
    def __init__(self, library):
        self.library: LibraryMediator = library

    def book_search(self, user: User, mode, key):
        try:
            return self.library.book_search(user, mode, key)
        except Exception as e:
            print(f"Error in book search: {e}")
            return []

    def book_borrow(self, user: User, book_id, days_borrowed):
        try:
            self.library.book_borrow(user, book_id, days_borrowed)
            return True
        except Exception as e:
            print(f"Error in book borrowing: {e}")
            return False

    def book_return(self, user: User, book_id):
        try:
            self.library.book_return(user, book_id)
            return True
        except Exception as e:
            print(f"Error in book return: {e}")
            return False

    def user_search(self, user: User, mode, key):
        try:
            return self.library.user_search(user, mode, key)
        except Exception as e:
            print(f"Error in user search: {e}")
            return []

    def book_add(self, user: User, book):
        try:
            self.library.book_add(user, book)
            return True
        except Exception as e:
            print(f"Error in adding book: {e}")
            return False
