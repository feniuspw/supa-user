from typing import Optional
from enum import Enum

from pydantic import BaseModel, EmailStr

class UserEmailPasswordAuth(BaseModel):
    email: EmailStr
    password: str


class UserPhonePasswordAuth(BaseModel):
    phone: str
    password: str

class OAuthProvider(str, Enum):
    """Supported OAuth providers for SSO."""

    GOOGLE = "google"
    MICROSOFT = "azure"
    GITHUB = "github"


class UserSSOAuth(BaseModel):
    provider: OAuthProvider
    redirect_to: Optional[str] = None


class SSOLoginResponse(BaseModel):
    redirect_url: str

class LoginResponse(BaseModel):
    user_id: str
    access_token: str
    refresh_token: str
    expires_in: int
    expires_at: int
