from sqlalchemy.orm import Session

from app.ml.models.user import User

from app.schemas.user_request import (
    UserCreateRequest,
    UserUpdateRequest,
    ChangePasswordRequest
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

def update_user(
    db: Session,
    user_id: int,
    payload: UserUpdateRequest
):

    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if user is None:
        return None

    user.full_name = payload.full_name
    user.email = payload.email
    user.phone = payload.phone
    user.address = payload.address
    if payload.role is not None:
        user.role = payload.role
    db.commit()

    db.refresh(user)

    return user


from app.core.security import (
    verify_password,
    hash_password
)

def change_password(
    db: Session,
    user_id: int,
    payload: ChangePasswordRequest
):

    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if user is None:
        return None

    if not verify_password(
        payload.old_password,
        user.password_hash
    ):
        return False

    user.password_hash = hash_password(
        payload.new_password
    )

    db.commit()

    return True


from datetime import datetime

def verify_email(
    db: Session,
    user_id: int
):

    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if user is None:
        return None

    user.email_verified_at = datetime.utcnow()

    db.commit()

    db.refresh(user)

    return user


def update_last_login(
    db: Session,
    user_id: int
):

    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if user is None:
        return

    user.last_login_at = datetime.utcnow()

    db.commit()


def disable_user(
    db: Session,
    user_id: int
):

    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if user is None:
        return None

    user.is_active = False

    db.commit()

    return user


def delete_user(
    db: Session,
    user_id: int
):

    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if user is None:
        return False

    db.delete(user)

    db.commit()

    return True