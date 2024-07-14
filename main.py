from database.DataBaseLocal import DataBaseLocal
from entities.Book import Book
from entities.users.StudentUserType import StudentUserType
from entities.users.TeacherUserType import TeacherUserType
from entities.users.LibrarianUserType import LibrarianUserType
from entities.users.User import User
from library.LibraryFacade import LibraryFacade
if __name__ == '__main__':

    db = DataBaseLocal()
    lib = LibraryFacade(db)

    book_1 = Book('Tittle 1', 'Author 1', 'Category 1')
    book_2 = Book('Tittle 2', 'Author 2', 'Category 2')
    book_3 = Book('Tittle 3', 'Author 3', 'Category 3')
    book_4 = Book('Tittle 4', 'Author 4', 'Category 4')
    book_5 = Book('Tittle 5', 'Author 5', 'Category 5')

    librarian_user = LibrarianUserType('Jack', 'Smith', 'jack03', 'jack03@mail.com', '3')
    db.add_user(librarian_user)
    lib.user_register('jack03', '3', 'John', 'Turner', 'john01', 'john01@mail.com', '1', 'student')
    lib.user_register('jack03', '3', 'Will', 'Tuk', 'will02', 'will02@mail.com', '2', 'teacher')

    lib.book_add('john01', '1', book_1)
    lib.book_add('will02', '2', book_2)
    lib.book_add('jack03', '3', book_3)

    print('Trying to search a book that does not exist')
    print(lib.book_search('jack03', '3', 'tittle', 'Tittle 1'))
    print('Trying to search a book that does not exist')
    print(lib.book_search('jack03', '3', 'tittle', 'Tittle 2'))
    print('Trying to search a book that exists')
    print(lib.book_search('jack03', '3', 'tittle', 'Tittle 3'))

    lib.book_delete('jack03', '3', book_3.id)

    print('Trying to search a deleted book')
    print(lib.book_search('will02', '2', 'tittle', 'Tittle 3'))

    lib.book_add('jack03', '3', book_1)
    lib.book_add('jack03', '3', book_2)
    lib.book_add('jack03', '3', book_3)
    lib.book_add('jack03', '3', book_4)
    lib.book_add('jack03', '3', book_5)

    print('Trying to borrow a book that exists')
    print(lib.book_borrow('john01', '1', book_1.id, 5))

    lib.book_return('will02', '2', book_1.id)

    print('Trying to search a user that exists')
    print(lib.user_search('jack03', '3', 'name', 'John Turner'))

