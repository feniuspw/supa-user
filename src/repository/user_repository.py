from abc import ABC, abstractmethod

class UserRepository(ABC):

    @abstractmethod
    def login_with_email_and_password(self, email: str, password: str):
        pass