from fastapi import APIRouter, HTTPException, status
from models.user import UserEmailPasswordAuth, LoginResponse
from adapters.supabase_adapter import SupabaseRepositoryAdapter
from services.auth_service import AuthService

router = APIRouter()
repository: SupabaseRepositoryAdapter = SupabaseRepositoryAdapter()

@router.post("/login-with-email-and-password", summary="Login with Email and Password", response_model=LoginResponse)
async def login_with_email_and_password(credentials: UserEmailPasswordAuth):
    try:
        session = AuthService(repository).login_with_email_and_password(credentials)
        return LoginResponse(
            user_id=session.user.id,
            access_token=session.session.access_token,
            refresh_token=session.session.refresh_token,
            expires_in=session.session.expires_in,
            expires_at=session.session.expires_at)
    except Exception as e:
        print(e)
        # Aqui você pode logar a exceção se quiser: print(e) ou logger.error(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")


    # Here, you would normally verify the credentials against your user service or database.
    # For demonstration purposes, we'll use a simple condition.
    # if credentials.email == "test@example.com" and credentials.password == "secret":
    #     return {"message": "Login successful"}
    # else:
    #     raise HTTPException(
    #         status_code=status.HTTP_401_UNAUTHORIZED,
    #         detail="Invalid email or password"
    #     )