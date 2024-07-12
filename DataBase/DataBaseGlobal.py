from Entities.users.User import User
from Library.LibraryMediator import LibraryMediator
from DataBaseLocal import DatabaseLocal

class DataBaseGlobal:
    def __init__(self):
        self.users = []
        self.libraries = []         #dataBaseLocal from each library on the catalog

    def add_user(self, user: User):
        self.users.append(user)

    def remove_user(self, user: User):
        if user in self.users:
            self.users.remove(user)

    def add_library(self, library: LibraryMediator):
        self.libraries.append(library)
    
    def remove_library(self, library: LibraryMediator):
        if library in self.libraries:
            self.libraries.remove(library)

    def get_library_database(self, library_name) -> DatabaseLocal:
        for library in self.libraries:
            if library.name == library_name:
                return library.database_local
        return None