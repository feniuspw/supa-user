from models.user import UserEmailPasswordAuth
from repository.user_repository import UserRepository


class AuthService:
    
    def __init__(self, repository: UserRepository):
        self.repository = repository
    
    def login_with_email_and_password(self, user_email_password_auth: UserEmailPasswordAuth):
        email: str = str(user_email_password_auth.email)
        password: str = user_email_password_auth.password
        return self.repository.login_with_email_and_password(email, password)
