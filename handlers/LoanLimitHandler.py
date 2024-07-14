from handlers.Handler import Handler


class LoanLimitHandler(Handler):
    def __init__(self, database, next_handler=None):
        super().__init__(next_handler)
        self.database = database

    def handle(self, request):
        user = request.get('user')
        user = self.database.get_user_by_id(user)
        loan_limit = user.permissions['borrow_limit']
        if len(self.database.get_borrowings_by_user(user.id)) < loan_limit:
            return super().handle(request)
        else:
            print("Exceeds loan limit for this user.")
            return False
