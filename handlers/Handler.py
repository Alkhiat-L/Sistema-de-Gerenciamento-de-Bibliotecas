from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def set_next(self, next_handler):
        self.next_handler = next_handler

    @abstractmethod
    def handle(self, request):
        if self.next_handler:
            return self.next_handler.handle(request)
        return False