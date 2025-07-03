from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date
from app.models.user import GenderEnum

# �򥻥Τ�[�c
class UserBase(BaseModel):
    email: EmailStr
    name: Optional[str] = None
    gender: Optional[GenderEnum] = None
    birth_date: Optional[date] = None
    phone: Optional[str] = None  # �s�W phone ���

# �Τ���U
class UserCreate(UserBase):
    password: str

# �Τ�n�J
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# �Τ�^�� - ��s���ǰt�s����Ʈw���c
class UserResponse(UserBase):
    # �����o�����A�]����Ʈw���w�g�S���F�G
    # id: int (email �{�b�O�D��)
    # is_active: bool (�w�R��)
    # is_verified: bool (�w�R��)
    
    # email �w�g�b UserBase ���w�q�F�A�@���D��
    
    class Config:
        from_attributes = True

# Token �[�c
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None