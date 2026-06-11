from pydantic import BaseModel
from pydantic import EmailStr


class UserCreateRequest(BaseModel):

    full_name: str

    username: str

    email: EmailStr

    password: str

    phone: str | None = None

    address: str | None = None


class UserUpdateRequest(BaseModel):

    full_name: str

    email: EmailStr

    phone: str | None = None

    address: str | None = None

    role: str | None = None


class ChangePasswordRequest(BaseModel):

    old_password: str

    new_password: str