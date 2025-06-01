from pydantic import BaseModel, EmailStr, Field


class UserModel(BaseModel):
    username: str = Field(..., min_length=3)
    email: EmailStr
    password: str = Field(..., min_length=8)