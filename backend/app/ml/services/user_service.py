from sqlalchemy.orm import Session

from app.ml.models.user import User

from app.schemas.user_request import (
    UserCreateRequest
)

from app.core.security import (
    hash_password
)

def create_user(
    db: Session,
    payload: UserCreateRequest
) -> User:

    user = User(

        full_name=payload.full_name,

        username=payload.username,

        email=payload.email,

        password_hash=hash_password(
            payload.password
        ),

        phone=payload.phone,

        address=payload.address,

        is_active=True
    )

    db.add(user)

    db.commit()

    db.refresh(user)

    return user

def get_user_by_id(
    db: Session,
    user_id: int
):

    return (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

def get_user_by_username(
    db: Session,
    username: str
):

    return (
        db.query(User)
        .filter(User.username == username)
        .first()
    )

def get_users(
    db: Session
):

    return (
        db.query(User)
        .all()
    )