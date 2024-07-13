from users.User import User


class BookAvailabilityNotifier:
    def __init__(self):
        self.observers: list[User] = []

    def add_observer(self, observer: User):
        self.observers.append(observer)

    def remove_observer(self, observer: User):
        self.observers.remove(observer)

    def notify(self, notify_type, book):
        for observer in self.observers:
            observer.update(notify_type, book)
