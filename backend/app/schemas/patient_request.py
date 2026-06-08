from datetime import date

from pydantic import BaseModel
from pydantic import EmailStr


class PatientCreateRequest(BaseModel):

    patient_name: str

    birth_date: date

    guardian_name: str

    guardian_email: EmailStr

    guardian_phone: str

    address: str | None = None