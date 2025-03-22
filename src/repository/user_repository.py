from abc import ABC, abstractmethod

class UserRepository(ABC):

    @abstractmethod
    def login_with_email_and_password(self, email: str, password: str):
        pass

    @abstractmethod
    def login_with_id_token(self, provider: str, token: str):
        pass