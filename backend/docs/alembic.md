# CARA MEMBUAT TABLE DENGAN ALEMBIC

Dipilihnya alembic karena memudahkan dalam pembuataan table bisa rollbac

## Persiapan

1. Menambahkan lib alembic pada requirements.txt

## Pembuatan kode

### Tabel yang akan digunakan

```text
users
    |
    | 1 : N
    |
patients
    |
    | 1 : N
    |
screenings
```

Karena:

- 1 user (orang tua/pendamping) bisa memiliki banyak pasien.
- 1 pasien bisa melakukan banyak screening.

Sangat cocok untuk aplikasi nyata.

Tabel users:

```text
 ------------------------------
| kolom         | tipe         |
| ------------- | ------------ |
| id            | bigint       |
| full_name     | varchar(255) |
| username      | varchar(100) |
| email         | varchar(255) |
| password_hash | varchar(255) |
| phone         | varchar(50)  |
| address       | text         |
| is_active     | boolean      |
| created_at    | datetime     |
| updated_at    | datetime     |
 ------------------------------
```

Kode app/ml/models/user.py

```python
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
```

Kode app/ml/models/patient.py

```python
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
```

Kode app/ml/models/screening.py

```python
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
```

jika sudah jalankan perintah seperti ini pada console fastapi:

```text
alembic revision --autogenerate -m "add users table and relation"
```

Jika sudah dilanjutkan perintah seperti berikut ini:

```text
alembic upgrade head
```
