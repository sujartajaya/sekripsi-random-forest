from datetime import date

from pydantic import BaseModel


class PatientCreateRequest(BaseModel):

    user_id: int

    patient_name: str

    birth_date: date