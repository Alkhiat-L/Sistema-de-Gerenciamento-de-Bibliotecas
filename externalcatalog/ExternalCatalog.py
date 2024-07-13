from abc import ABC, abstractmethod

class ExternalCatalog(ABC):
    @abstractmethod
    def search_books(self, mode, key):
        pass

    @abstractmethod
    def borrow_book(self, user_id, book_id, days_borrowed):
        pass

    @abstractmethod
    def return_book(self, user_id, book_id):
        pass

    @abstractmethod
    def search_users(self, mode, key):
        pass