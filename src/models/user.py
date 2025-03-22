from typing import Optional

from pydantic import BaseModel, EmailStr

class UserEmailPasswordAuth(BaseModel):
    email: EmailStr
    password: str


class UserPhonePasswordAuth(BaseModel):
    phone: str
    password: str

class UserSSOAuth(BaseModel):
    provider: str
    redirect_to: Optional[str] = None

class LoginResponse(BaseModel):
    user_id: str
    access_token: str
    refresh_token: str
    expires_in: int
    expires_at: int