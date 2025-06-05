import os
from supabase import create_client

from adapters.exceptions.supabase_exceptions import SupabaseLoginException
from repository.user_repository import UserRepository


class SupabaseRepositoryAdapter(UserRepository):

    def __init__(self):
        url = os.environ.get("SUPABASE_URL")
        key = os.environ.get("SUPABASE_API_KEY")
        if not url or not key:
            raise ValueError("SUPABASE_URL and SUPABASE_API_KEY must be set")
        self.client = create_client(url, key)

    def login_with_email_and_password(self, email: str, password: str):
        """
        Log in an existing user with an email and password.
        """
        try:
            return self.client.auth.sign_in_with_password({
                "email": email,
                "password": password
            })
        except Exception as e:
            raise SupabaseLoginException(
                f"Failed logging in to Supabase using email and password: {e}"
            )

    def login_with_phone_and_password(self, phone: str, password: str):
        """
        Log in an existing user with a phone and password.
        """
        try:
            return self.client.auth.sign_in_with_password({
                "phone": phone,
                "password": password
            })
        except Exception as e:
            raise SupabaseLoginException(
                f"Failed logging in to Supabase using phone and password: {e}"
            )


    def login_with_id_token(self, provider: str, token: str):
        """
        Allows signing in with an OIDC ID token.
        The authentication provider used should be enabled and configured.
        """
        try:
            return self.client.auth.sign_in_with_id_token({
                "provider": provider,
                "token": token
            })
        except Exception as e:
            raise SupabaseLoginException(f"Failed Logging in to Supabase using provider {provider}: {e}")

    def login_with_oauth(self, provider: str, redirect_to: str | None = None):
        """Log in using OAuth provider returning the redirect URL."""
        try:
            options = {"provider": provider}
            if redirect_to:
                options["redirect_to"] = redirect_to
            return self.client.auth.sign_in_with_oauth(options)
        except Exception as e:
            raise SupabaseLoginException(
                f"Failed Logging in to Supabase using oauth provider {provider}: {e}"
            )
