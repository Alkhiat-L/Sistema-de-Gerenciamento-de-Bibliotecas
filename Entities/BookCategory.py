from Entities.Book import Book

class BookCategory:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.subcategories = []
        self.books = []

    def add_subcategory(self, subcategory):
        if isinstance(subcategory, BookCategory):
            self.subcategories.append(subcategory)
        else:
            raise Exception("Parameter is not type 'BookCategory'")
        
    def remove_subcategory(self, subcategory):
        if subcategory in self.subcategories:
            self.subcategories.remove(subcategory)
        else:
            raise Exception(f"{subcategory.name} not found in subcategories.")

    def get_subcategories(self):
        return self.subcategories
    
    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise Exception("Parameter is not of type 'Book'")
        
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
        else:
            raise Exception(f"{book.title} not found in category.")
    
    def get_books(self):
        return self.books
    
    def belongs_to_category(self, category_name):
        if self.name == category_name:
            return True
        for subcategory in self.subcategories:
            if subcategory.belongs_to_category(category_name):
                return True
        return False