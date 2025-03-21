from typing import Optional
from pydantic import BaseModel, EmailStr

class UserEmailPasswordAuth(BaseModel):
    email: EmailStr
    password: str

class UserSSOAuth(BaseModel):
    provider: str
    redirect_to: Optional[str] = None
