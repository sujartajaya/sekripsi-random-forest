from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict


class UserResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    full_name: str

    username: str

    email: str

    phone: str | None

    address: str | None

    is_active: bool

    last_login_at: datetime | None
    
    created_at: datetime

    updated_at: datetime