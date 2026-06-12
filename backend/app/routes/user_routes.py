from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.dependencies import get_db

from app.schemas.user_request import (
    UserCreateRequest
)

from app.schemas.user_response import (
    UserResponse
)

from app.ml.services.user_service import (
    create_user,
    get_user_by_id,
    get_users
)

from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database import get_db

from app.ml.services.user_service import (
    send_verify_email
)

from app.core.auth import get_current_user


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post(
    "",
    response_model=UserResponse
)
def create_user_route(
    payload: UserCreateRequest,
    db: Session = Depends(get_db)
):

    return create_user(
        db=db,
        payload=payload
    )

@router.get(
    "/{user_id}",
    response_model=UserResponse
)
def get_user_route(
    user_id: int,
    db: Session = Depends(get_db)
):

    return get_user_by_id(
        db=db,
        user_id=user_id
    )

from typing import List

@router.get(
    "",
    response_model=List[UserResponse]
)
def list_users(
    db: Session = Depends(get_db)
):

    return get_users(db)


@router.post(
    "/send-verification-email"
)
def send_verification_email(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    result = send_verify_email(
        db,
        current_user.id
    )

    if result is None:

        raise HTTPException(
            status_code=404,
            detail="User tidak ditemukan"
        )

    if result == "verified":

        raise HTTPException(
            status_code=400,
            detail="Email sudah terverifikasi"
        )

    return {
        "status": "success",
        "message": "Email verifikasi berhasil dikirim"
    }