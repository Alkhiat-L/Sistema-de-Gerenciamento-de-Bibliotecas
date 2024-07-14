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
        if notify_type == 'book_added' and self.observers.get('book_added'):
            self.send_notification('The book ' + book.title + ' was added to the library')
        if notify_type == 'book_removed' and self.observers.get('book_removed'):
            self.send_notification('The book ' + book.title + ' was removed from the library')
        if notify_type == 'book_borrowed' and self.observers.get('book_borrowed'):
            self.send_notification('The book ' + book.title + ' was borrowed')
        if notify_type == 'book_returned' and self.observers.get('book_returned'):
            self.send_notification('The book ' + book.title + ' was returned to the library')

    def send_notification(self, message):
        #notification = generate_id()
        #send_notification_email(notification)
        print(f"Notification to {self.email}: {message}")