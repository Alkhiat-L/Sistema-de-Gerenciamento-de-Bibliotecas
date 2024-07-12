from User import User


class StudentUserType(User):
    def __init__(self, first_name, last_name, username, email, password):
        super().__init__(first_name, last_name, username, email, password)
        self.permissions = {
            'borrow': 3,
            'return': True,
            'book_search': True,
            'user_search': 0,
            'add_book': False,
            'remove_book': False
        }