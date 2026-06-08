from sqlalchemy import (
    Column,
    BigInteger,
    String,
    Date,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship

from sqlalchemy.sql import func

from app.core.database import Base


class Patient(Base):

    __tablename__ = "patients"

    id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )

    user_id = Column(
        BigInteger,
        ForeignKey("users.id"),
        nullable=False
    )

    patient_name = Column(
        String(255),
        nullable=False
    )

    birth_date = Column(
        Date,
        nullable=False
    )

    created_at = Column(
        DateTime,
        server_default=func.now()
    )

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )

    user = relationship(
        "User",
        back_populates="patients"
    )

    screenings = relationship(
        "Screening",
        back_populates="patient"
    )