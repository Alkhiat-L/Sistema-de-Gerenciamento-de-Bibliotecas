from handlers.Handler import Handler

class BorrowLimitHandler(Handler):
    def __init__(self, database, next_handler=None):
        super().__init__(next_handler)
        self.database = database
        self.last = False

    def set_last(self, last):
        self.last = last

    def handle(self, request):
        user = request.get('user')
        borrow_limit = user.permissions['borrow_limit']
        if len(self.database.get_borrowings_by_user(user.id)) < borrow_limit:
            return super().handle(request)
        else:
            print("Exceeds borrow limit for this user.")
            return False
