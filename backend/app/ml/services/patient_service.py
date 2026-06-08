from sqlalchemy.orm import Session

from app.ml.models.patient import Patient

from app.schemas.patient_request import (
    PatientCreateRequest
)


def create_patient(
    db: Session,
    payload: PatientCreateRequest
) -> Patient:

    patient = Patient(

        patient_name=payload.patient_name,

        birth_date=payload.birth_date,

        guardian_name=payload.guardian_name,

        guardian_email=payload.guardian_email,

        guardian_phone=payload.guardian_phone,

        address=payload.address
    )

    db.add(patient)

    db.commit()

    db.refresh(patient)

    return patient

def get_patient_by_id(
    db: Session,
    patient_id: int
) -> Patient | None:

    return (
        db.query(Patient)
        .filter(Patient.id == patient_id)
        .first()
    )