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

        user_id=payload.user_id,

        patient_name=payload.patient_name,

        birth_date=payload.birth_date

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


def get_patients(
    db: Session
):

    return (

        db.query(Patient)

        .all()

    )


def get_patients_by_user(
    db: Session,
    user_id: int
):

    return (

        db.query(Patient)

        .filter(
            Patient.user_id == user_id
        )

        .all()

    )

def delete_patient(
    db: Session,
    patient_id: int
):

    patient = (

        db.query(Patient)

        .filter(
            Patient.id == patient_id
        )

        .first()

    )

    if patient:

        db.delete(patient)

        db.commit()

    return patient

def find_patient(
    db: Session,
    user_id: int,
    patient_name: str,
    birth_date
) -> Patient | None:

    return (
        db.query(Patient)
        .filter(
            Patient.user_id == user_id,
            Patient.patient_name == patient_name,
            Patient.birth_date == birth_date
        )
        .first()
    )

def update_patient(
    db: Session,
    patient_id: int,
    payload: PatientCreateRequest
) -> Patient | None:

    patient = (
        db.query(Patient)
        .filter(
            Patient.id == patient_id
        )
        .first()
    )

    if patient is None:
        return None

    patient.user_id = payload.user_id
    patient.patient_name = payload.patient_name
    patient.birth_date = payload.birth_date

    db.commit()

    db.refresh(patient)

    return patient