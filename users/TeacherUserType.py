from User import  User


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