import os
from models.user import UserEmailPasswordAuth, UserSSOAuth
from repository.user_repository import UserRepository


class AuthService:
    
    def __init__(self, repository: UserRepository):
        self.repository = repository
    
    def login_with_email_and_password(self, user_email_password_auth: UserEmailPasswordAuth):
        email: str = str(user_email_password_auth.email)
        password: str = user_email_password_auth.password
        return self.repository.login_with_email_and_password(email, password)

    def login_with_sso(self, user_sso_auth: UserSSOAuth):
        provider = user_sso_auth.provider
        redirect_to = user_sso_auth.redirect_to or os.environ.get("SSO_REDIRECT_TO")
        return self.repository.login_with_oauth(provider, redirect_to)

