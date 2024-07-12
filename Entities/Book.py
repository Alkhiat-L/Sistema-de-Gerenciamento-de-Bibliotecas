import random

from BookCategory import BookCategory

class Book:
    def __init__(self, title, author, category: BookCategory):
        self.title = title
        self.author = author
        self.category = category
        self.available = True
        self.id = None
        self.borrowed_by = None
        self.return_date = None

    def generate_id(self):
        prefix = "Book_"
        random_suffix = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=8))
        self.id = prefix + random_suffix

    def belongs_to_category(self, category_name):
        return self.category.belongs_to_category(category_name)