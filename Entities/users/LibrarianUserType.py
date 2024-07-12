from User import  User

import random

class LibrarianUserType(User):
    def __init__(self, first_name, last_name, username, email, password):
        super().__init__(first_name, last_name, username, email, password)
        self.permissions = {
            'borrow': 3,
            'return': True,
            'book_search': True,
            'user_search': 2,
            'add_book': True,
            'remove_book': True
        }

    def generate_id(self):
        prefix = "Librarian_"
        random_suffix = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=8))
        self.id = prefix + random_suffix
        return self.id