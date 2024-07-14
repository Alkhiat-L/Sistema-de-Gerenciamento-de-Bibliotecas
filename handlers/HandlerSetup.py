from database.DataBaseLocal import DataBaseLocal
from handlers.BookAvailabilityHandler import BookAvailabilityHandler
from handlers.BorrowedTimeHandler import BorrowedTimeHandler
from handlers.BorrowLimitHandler import BorrowLimitHandler


class HandlerSetup:
    def __init__(self, database):
        self.database = database
        self.head = None

    def setup_chain(self):
        book_availability_handler = BookAvailabilityHandler(self.database)
        borrowed_time_handler = BorrowedTimeHandler(self.database)
        borrow_limit_handler = BorrowLimitHandler(self.database)

        # Set up the chain
        borrow_limit_handler.set_last(True)
        book_availability_handler.set_next(borrowed_time_handler)
        borrowed_time_handler.set_next(borrow_limit_handler)

        # Set the head of the chain
        self.head = book_availability_handler
        return self.head

    def handle_request(self, user, book_id, days_borrowed):
        if self.head is None:
            raise RuntimeError("Chain has no handlers")

        request = {'user': user, 'book': book_id, 'days_borrowed': days_borrowed}
        return self.head.handle(request)
