from typing import List

from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.dependencies import get_db

from app.schemas.patient_request import (
    PatientCreateRequest
)

from app.schemas.patient_response import (
    PatientResponse
)

from app.ml.services.patient_service import (
    create_patient,
    get_patient_by_id,
    get_patients,
    get_patients_by_user,
    delete_patient,
    update_patient
)

router = APIRouter(
    prefix="/patients",
    tags=["Patients"]
)

@router.post(
    "",
    response_model=PatientResponse
)
def create_patient_route(
    payload: PatientCreateRequest,
    db: Session = Depends(get_db)
):

    return create_patient(
        db=db,
        payload=payload
    )

    return patient


@router.get(
    "",
    response_model=List[PatientResponse]
)
def list_patients(
    db: Session = Depends(get_db)
):

    return get_patients(db)

@router.get(
    "/{patient_id}",
    response_model=PatientResponse
)
def get_patient_route(
    patient_id: int,
    db: Session = Depends(get_db)
):

    return get_patient_by_id(
        db=db,
        patient_id=patient_id
    )

@router.get(
    "/user/{user_id}",
    response_model=List[PatientResponse]
)
def get_patient_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    return get_patients_by_user(
        db=db,
        user_id=user_id
    )

@router.delete(
    "/{patient_id}"
)
def delete_patient_route(
    patient_id: int,
    db: Session = Depends(get_db)
):

    delete_patient(
        db=db,
        patient_id=patient_id
    )

    return {
        "status": "success"
    }


@router.put(
    "/{patient_id}"
)
def update_patient_route(
    patient_id: int,
    payload: PatientCreateRequest,
    db: Session = Depends(get_db)
):

    return update_patient(
        db=db,
        patient_id=patient_id,
        payload=payload
    )