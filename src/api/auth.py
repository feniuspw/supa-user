from fastapi import APIRouter, HTTPException, status
from models.user import UserEmailPasswordAuth
from adapters.supabase_adapter import SupabaseRepositoryAdapter
from services.auth_service import AuthService

router = APIRouter()
repository: SupabaseRepositoryAdapter = SupabaseRepositoryAdapter()

@router.post("/login-with-email-and-password", summary="Login with Email and Password")
async def login_with_email_and_password(credentials: UserEmailPasswordAuth):
    user_logged = AuthService(repository).login_with_email_and_password(credentials)






    # Here, you would normally verify the credentials against your user service or database.
    # For demonstration purposes, we'll use a simple condition.
    # if credentials.email == "test@example.com" and credentials.password == "secret":
    #     return {"message": "Login successful"}
    # else:
    #     raise HTTPException(
    #         status_code=status.HTTP_401_UNAUTHORIZED,
    #         detail="Invalid email or password"
    #     )