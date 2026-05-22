from pydantic import BaseModel


class PredictRequest(BaseModel):

    A1_Score: bool
    A2_Score: bool
    A3_Score: bool
    A4_Score: bool
    A5_Score: bool
    A6_Score: bool
    A7_Score: bool
    A8_Score: bool
    A9_Score: bool
    A10_Score: bool

    age: int

    gender: str

    ethnicity: str

    jundice: bool

    austim: bool

    used_app_before: bool

    relation: str