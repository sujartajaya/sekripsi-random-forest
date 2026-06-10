from pydantic import BaseModel
from pydantic import EmailStr


class UserCreateRequest(BaseModel):

    full_name: str

    username: str

    email: EmailStr

    password: str

    phone: str | None = None

    address: str | None = None