import logging
from fastapi import APIRouter, HTTPException, status, Depends
from models.user import UserEmailPasswordAuth, LoginResponse, UserSSOAuth, SSOLoginResponse
from services.auth_service import AuthService
from adapters.supabase_adapter import SupabaseRepositoryAdapter
from settings import Settings, get_settings

router = APIRouter()
logger = logging.getLogger(__name__)


def get_auth_service(settings: Settings = Depends(get_settings)) -> AuthService:
    repository = SupabaseRepositoryAdapter(settings)
    return AuthService(repository, settings)

@router.post(
    "/login-with-email-and-password",
    summary="Login with Email and Password",
    response_model=LoginResponse,
)
async def login_with_email_and_password(
    credentials: UserEmailPasswordAuth,
    service: AuthService = Depends(get_auth_service),
):
    try:
        session = service.login_with_email_and_password(credentials)
        return LoginResponse(
            user_id=session.user.id,
            access_token=session.session.access_token,
            refresh_token=session.session.refresh_token,
            expires_in=session.session.expires_in,
            expires_at=session.session.expires_at,
        )
    except Exception:
        logger.exception("login_with_email_and_password failed")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )


@router.post("/login-with-sso", summary="Login with Gmail SSO", response_model=SSOLoginResponse)
async def login_with_sso(
    credentials: UserSSOAuth,
    service: AuthService = Depends(get_auth_service),
):
    try:
        response = service.login_with_sso(credentials)
        return SSOLoginResponse(redirect_url=response.get("url"))
    except Exception:
        logger.exception("login_with_sso failed")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )


    # Here, you would normally verify the credentials against your user service or database.
    # For demonstration purposes, we'll use a simple condition.
    # if credentials.email == "test@example.com" and credentials.password == "secret":
    #     return {"message": "Login successful"}
    # else:
    #     raise HTTPException(
    #         status_code=status.HTTP_401_UNAUTHORIZED,
    #         detail="Invalid email or password"
    #     )
