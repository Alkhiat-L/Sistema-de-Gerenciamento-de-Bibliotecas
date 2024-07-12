from User import  User

import random

class TeacherUserType(User):
    def __init__(self, first_name, last_name, username, email, password):
        super().__init__(first_name, last_name, username, email, password)
        self.permissions = {
            'borrow': 5,
            'return': True,
            'book_search': True,
            'user_search': 1,
            'add_book': False,
            'remove_book': False
        }

    def generate_id(self):
        prefix = "Professor_"
        random_suffix = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=8))
        self.id = prefix + random_suffix
        return self.id