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
    create_patient, get_patient_by_id
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

@router.get(
    "/{patient_id}",
    response_model=PatientResponse
)

def get_patient(
    patient_id: int,
    db: Session = Depends(get_db)
):

    patient = get_patient_by_id(
        db=db,
        patient_id=patient_id
    )

    return patient


