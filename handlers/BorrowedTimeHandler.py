from handlers.Handler import Handler

class BorrowedTimeHandler(Handler):
    def __init__(self, database, next_handler=None):
        super().__init__(next_handler)
        self.database = database

    def handle(self, request):
        days_borrowed = request.get('days_borrowed')
        if days_borrowed < self.database.maxDaysBorrowed:
            return super().handle(request)
        else:
            print("Borrow time longer than the max time of the library.")
            return False