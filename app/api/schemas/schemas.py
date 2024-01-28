# schemas.py
from pydantic import UUID4, BaseModel
from typing import Optional, List


class UserBase(BaseModel):
    name: str
    email: str


class Movie(BaseModel):
    title: str
    overview: str
    media_type: str
    popularity: float


class Creator(BaseModel):
    name: str
    known_for_department: str
    movies: List[Movie]


class UserCreate(UserBase):
    password: str
    password_confirmation: str
    is_admin: bool = False


class UserUpdate(UserBase):
    pass


class User(UserBase):
    id: UUID4

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
