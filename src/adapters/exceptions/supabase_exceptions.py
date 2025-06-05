class SupabaseException(Exception):
    def __init__(self, message: str = "An error occurred with Supabase"):
        super().__init__(message)

class SupabaseLoginException(SupabaseException):
    def __init__(self, message: str = "Login failed with Supabase"):
        super().__init__(message)

