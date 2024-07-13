from Entities.BookAvailabilityNotifier import BookAvailabilityNotifier
from config.ConfigurationManager import ConfigurationManager


class User:
    def __init__(self, first_name, last_name, username, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password
        self.id = self.generate_id()
        self.books = []
        self.observers = ConfigurationManager().get_user_observers()
        self.permissions = self.permissions = ConfigurationManager().get_user_permissions('user')

    def set_observers(self, added: bool, removed: bool, borrowed: bool, returned: bool):
        if added is not None:
            self.observers['book_added'] = added
        if removed is not None:
            self.observers['book_removed'] = removed
        if borrowed is not None:
            self.observers['book_borrowed'] = borrowed
        if returned is not None:
            self.observers['book_returned'] = returned

    def update(self, notify_type, book):
        if notify_type == 'book_added' and self.observers['book_added']:
            pass
            #sendmessage(user.email, 'The book ' + book.tittle + ' was added to the library')
        if notify_type == 'book_removed' and self.observers['book_removed']:
            pass
            #sendmessage(user.email, 'The book ' + book.tittle + ' was removed from the library')
        if notify_type == 'book_borrowed' and self.observers['book_borrowed']:
            pass
            #sendmessage(user.email, 'The book ' + book.tittle + ' was borrowed')
        if notify_type == 'book_returned' and self.observers['book_returned']:
            pass
            #sendmessage(user.email, 'The book ' + book.tittle + ' was returned to the library')

    def generate_id(self):
        return None