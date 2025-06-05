import logging
from supabase import create_client

from adapters.exceptions.supabase_exceptions import SupabaseLoginException
from repository.user_repository import UserRepository
from settings import Settings


logger = logging.getLogger(__name__)


class SupabaseRepositoryAdapter(UserRepository):

    def __init__(self, settings: Settings):
        try:
            self.client = create_client(settings.SUPABASE_URL, settings.SUPABASE_API_KEY)
            logger.debug("Supabase client initialized")
        except Exception as e:
            logger.exception("Failed to initialize Supabase client")
            raise

    def login_with_email_and_password(self, email: str, password: str):
        """
        Log in an existing user with an email and password.
        """
        try:
            logger.info("Logging in user with email")
            return self.client.auth.sign_in_with_password({
                "email": email,
                "password": password
            })
        except Exception as e:
            logger.exception("Email/password login failed")
            raise SupabaseLoginException(
                f"Failed logging in to Supabase using email and password: {e}"
            )

    def login_with_phone_and_password(self, phone: str, password: str):
        """
        Log in an existing user with a phone and password.
        """
        try:
            logger.info("Logging in user with phone")
            return self.client.auth.sign_in_with_password({
                "phone": phone,
                "password": password
            })
        except Exception as e:
            logger.exception("Phone/password login failed")
            raise SupabaseLoginException(
                f"Failed logging in to Supabase using phone and password: {e}"
            )


    def login_with_id_token(self, provider: str, token: str):
        """
        Allows signing in with an OIDC ID token.
        The authentication provider used should be enabled and configured.
        """
        try:
            logger.info("Logging in user with id token provider %s", provider)
            return self.client.auth.sign_in_with_id_token({
                "provider": provider,
                "token": token
            })
        except Exception as e:
            logger.exception("ID token login failed")
            raise SupabaseLoginException(f"Failed Logging in to Supabase using provider {provider}: {e}")

    def login_with_oauth(self, provider: str, redirect_to: str | None = None):
        """Log in using OAuth provider returning the redirect URL."""
        try:
            logger.info("Logging in user with oauth provider %s", provider)
            options = {"provider": provider}
            if redirect_to:
                options["redirect_to"] = redirect_to
            return self.client.auth.sign_in_with_oauth(options)
        except Exception as e:
            logger.exception("OAuth login failed")
            raise SupabaseLoginException(
                f"Failed Logging in to Supabase using oauth provider {provider}: {e}"
            )
