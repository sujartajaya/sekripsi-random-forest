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

import secrets

from datetime import (
    datetime,
    timedelta
)

from app.core.email import send_email
from app.core.settings import settings

from app.core.security import (
    verify_password,
    create_access_token
)

from app.schemas.user_request import (
    LoginRequest
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

        is_active=False
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
    token: str
):

    user = (
        db.query(User)
        .filter(
            User.verify_email_token == token
        )
        .first()
    )

    if user is None:
        return None

    if (
        user.verify_email_expired_at
        < datetime.utcnow()
    ):
        return None

    user.email_verified_at = datetime.utcnow()

    user.verify_email_token = None
    user.verify_email_expired_at = None

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


# Send email verification
def send_verify_email(
    db: Session,
    user_id: int
):

    user = (
        db.query(User)
        .filter(
            User.id == user_id
        )
        .first()
    )

    if user is None:
        return None

    if user.email_verified_at is not None:
        return "verified"

    token = secrets.token_urlsafe(32)

    user.verify_email_token = token

    user.verify_email_expired_at = (
        datetime.utcnow()
        + timedelta(minutes=30)
    )

    db.commit()

    verify_url = (
        f"{settings.FRONTEND_URL}"
        f"/verify-email"
        f"?token={token}"
    )

    html = f"""
    <h2>Verifikasi Email</h2>

    <p>Halo {user.full_name}</p>

    <p>
        Klik tombol berikut untuk verifikasi email:
    </p>

    <a href="{verify_url}">
        Verifikasi Email
    </a>

    <p>
        Link berlaku selama 30 menit.
    </p>
    """

    send_email(
        to_email=user.email,
        subject="Verifikasi Email",
        html=html
    )

    return True


def login(
    db: Session,
    payload: LoginRequest
):

    user = (
        db.query(User)
        .filter(
            User.username == payload.username
        )
        .first()
    )

    if user is None:
        return None

    if not verify_password(
        payload.password,
        user.password_hash
    ):
        return False

    token = create_access_token(
        {
            "user_id": user.id
        }
    )

    update_last_login(
        db=db,
        user_id=user.id
    )

    return {
        "access_token": token,
        "token_type": "Bearer",
        "user": user
    }