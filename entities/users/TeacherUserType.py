from entities.users.User import User
from config.ConfigurationManager import ConfigurationManager
import random


class TeacherUserType(User):
    def __init__(self, first_name, last_name, username, email, password):
        super().__init__(first_name, last_name, username, email, password)
        self.permissions = self.permissions = ConfigurationManager().get_user_permissions('teacher')

    def generate_id(self):
        prefix = "Professor_"
        random_suffix = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=8))
        self.id = prefix + random_suffix
        return self.id