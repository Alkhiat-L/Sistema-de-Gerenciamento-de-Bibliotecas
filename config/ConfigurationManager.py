class ConfigurationManager:
    def __init__(self):
        self.borrow_config = {
            'librarian': False,
            'user': True,
            'student': True,
            'teacher': True
        }
        self.borrow_limit = {
            'librarian': 0,
            'user': 0,
            'student': 3,
            'teacher': 5
        }
        self.return_config = {
            'librarian': False,
            'user': True,
            'student': True,
            'teacher': True
        }
        self.book_search_config = {
            'librarian': True,
            'user': True,
            'student': True,
            'teacher': True
        }
        self.user_search_config = {
            'librarian': 2,
            'user': 0,
            'student': 0,
            'teacher': 1
        }
        self.add_book_config = {
            'librarian': True,
            'user': False,
            'student': False,
            'teacher': False
        }
        self.remove_book_config = {
            'librarian': True,
            'user': False,
            'student': False,
            'teacher': False
        }
        self.register_user_config = {
            'librarian': True,
            'user': False,
            'student': False,
            'teacher': False
        }
        self.default_users_observers = {
            'book_added': True,
            'book_removed': True,
            'book_borrowed': False,
            'book_returned': False
        }

    def get_user_observers(self):
        return self.default_users_observers

    def get_user_permissions(self, user_type):
        return {
            'borrow': self.borrow_config[user_type],
            'return': self.return_config[user_type],
            'book_search': self.book_search_config[user_type],
            'user_search': self.user_search_config[user_type],
            'add_book': self.add_book_config[user_type],
            'remove_book': self.remove_book_config[user_type],
            'register_user': self.register_user_config[user_type],
            'borrow_limit': self.borrow_limit[user_type]
        }
