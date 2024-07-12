class User:
    def __init__(self, first_name, last_name, username, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password
        self.id = self.generate_id()
        self.books = []
        self.permissions = {
            'borrow': 1,
            'return': True,
            'book_search': True,
            'user_search': 0,
            'add_book': False,
            'remove_book': False
        }

    def generate_id(self):
        return None