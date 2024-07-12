from LibraryMediator import LibraryMediator


class LibraryFacade:
    def __init__(self, library):
        self.library: LibraryMediator = library

    def book_search(self, user, mode, key):
        books = self.library.book_search(user, mode, key)
        print(books)

    def book_borrow(self, user, book, days_borrowed):
        self.library.book_borrow(user, book, days_borrowed)

    def book_return(self, user, book):
        self.library.book_return(user, book)

    def user_search(self, user, mode, key):
        users = self.library.user_search(user, mode, key)
        print(users)

    def book_add(self, user, book):
        self.library.book_add(user, book)
