from sqlalchemy import (
    Column,
    BigInteger,
    String,
    Boolean,
    DateTime,
    Text
)

from sqlalchemy.orm import relationship

from sqlalchemy.sql import func

from app.core.database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )

    full_name = Column(
        String(255),
        nullable=False
    )

    username = Column(
        String(100),
        nullable=False,
        unique=True
    )

    email = Column(
        String(255),
        nullable=False,
        unique=True
    )

    password_hash = Column(
        String(255),
        nullable=False
    )

    phone = Column(
        String(50),
        nullable=True
    )

    address = Column(
        Text,
        nullable=True
    )

    is_active = Column(
        Boolean,
        default=True
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

    patients = relationship(
        "Patient",
        back_populates="user"
    )