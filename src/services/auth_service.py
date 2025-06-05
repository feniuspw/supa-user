import logging
from models.user import UserEmailPasswordAuth, UserSSOAuth
from repository.user_repository import UserRepository
from settings import Settings


logger = logging.getLogger(__name__)


class AuthService:

    def __init__(self, repository: UserRepository, settings: Settings):
        self.repository = repository
        self.settings = settings
    
    def login_with_email_and_password(self, user_email_password_auth: UserEmailPasswordAuth):
        email: str = str(user_email_password_auth.email)
        password: str = user_email_password_auth.password
        logger.debug("AuthService login_with_email_and_password for %s", email)
        return self.repository.login_with_email_and_password(email, password)

    def login_with_sso(self, user_sso_auth: UserSSOAuth):
        provider = user_sso_auth.provider
        redirect_to = user_sso_auth.redirect_to or self.settings.SSO_REDIRECT_TO
        logger.debug(
            "AuthService login_with_sso using provider %s and redirect %s", provider, redirect_to
        )
        return self.repository.login_with_oauth(provider, redirect_to)

