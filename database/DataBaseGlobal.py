from typing import List

from entities.users.User import User
from library.LibraryMediator import LibraryMediator
from DataBaseLocal import DataBaseLocal

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

    def get_all_database_library(self) -> List[DataBaseLocal]:
        all_database_library = []
        for library in self.libraries:
            all_database_library.append(library)
        return all_database_library

    def get_library_database(self, library_name) -> DataBaseLocal:
        for library in self.libraries:
            if library.name == library_name:
                return library.database_local
        return None
    
    def get_user_by_username(self, username: str) -> User:
        for user in self.users:
            if user.username == username:
                return user
        return None

    def get_user_by_email(self, email: str) -> User:
        for user in self.users:
            if user.email == email:
                return user
        return None

    def get_user_by_id(self, user_id: int) -> User:
        for user in self.users:
            if user.id == user_id:
                return user
        return None