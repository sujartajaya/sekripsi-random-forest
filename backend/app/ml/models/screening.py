from sqlalchemy import (
    Column,
    BigInteger,
    Integer,
    String,
    Boolean,
    DateTime,
    DECIMAL,
    ForeignKey
)

from sqlalchemy.orm import relationship

from sqlalchemy.sql import func

from app.core.database import Base


class Screening(Base):

    __tablename__ = "screenings"

    id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )

    patient_id = Column(
        BigInteger,
        ForeignKey("patients.id"),
        nullable=False
    )

    A1_Score = Column(Boolean)
    A2_Score = Column(Boolean)
    A3_Score = Column(Boolean)
    A4_Score = Column(Boolean)
    A5_Score = Column(Boolean)
    A6_Score = Column(Boolean)
    A7_Score = Column(Boolean)
    A8_Score = Column(Boolean)
    A9_Score = Column(Boolean)
    A10_Score = Column(Boolean)

    age = Column(Integer)

    gender = Column(String(50))

    ethnicity = Column(String(100))

    jundice = Column(Boolean)

    austim = Column(Boolean)

    used_app_before = Column(Boolean)

    relation = Column(String(100))

    prediction = Column(Integer)

    probability = Column(
        DECIMAL(5, 2)
    )

    created_at = Column(
        DateTime,
        server_default=func.now()
    )

    patient = relationship(
        "Patient",
        back_populates="screenings"
    )