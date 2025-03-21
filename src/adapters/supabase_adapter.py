import os
from supabase import create_client

from adapters.exceptions.supabase_exceptions import SupabaseLoginException
from repository.user_repository import UserRepository


class SupabaseRepositoryAdapter(UserRepository):
    def __init__(self):
        url = os.environ.get("SUPABASE_URL")
        key = os.environ.get("SUPABASE_API_KEY")
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
            raise SupabaseLoginException(f"Failed Loging in to Supabase using email and password: {e}")

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
            raise SupabaseLoginException(f"Failed Loging in to Supabase using phone and password: {e}")

