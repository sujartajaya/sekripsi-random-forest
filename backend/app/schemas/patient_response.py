from datetime import datetime
from datetime import date

from pydantic import BaseModel
from pydantic import ConfigDict


class PatientResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    patient_name: str

    birth_date: date

    guardian_name: str

    guardian_email: str

    guardian_phone: str

    address: str | None

    created_at: datetime
    updated_at: datetime