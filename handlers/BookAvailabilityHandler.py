from handlers import Handler

class BookAvailabilityHandler(Handler):
    def __init__(self, database, next_handler=None):
        super().__init__(next_handler)
        self.database = database

    def handle(self, request):
        book_id = request.get('book')
        book = self.database.get_book_by_id(book_id)
        if book and book.available:
            return super().handle(request)
        else:
            print("Book is not available.")
            return False
