from datetime import date

import sqlalchemy as sa

from app.adapters.storage.db.base_model import BaseModel


class Specialization(BaseModel):
    """Специальность."""

    __tablename__ = "specializations"

    id: int = sa.Column(sa.BigInteger(), primary_key=True, autoincrement=True)
    name: str = sa.Column(sa.String(length=30), nullable=False)


class Specialist(BaseModel):
    """Специалист."""

    __tablename__ = "specialists"

    id: int = sa.Column(sa.BigInteger(), primary_key=True, autoincrement=True)
    name: str = sa.Column(sa.String(length=50), nullable=False)
    photo: str = sa.Column(sa.String(length=150), nullable=True)
    start_work_date: date = sa.Column(sa.Date(), nullable=False)
    description: str = sa.Column(sa.Text())
    on_main: bool = sa.Column(sa.Boolean(), default=False)


specializations_specialists_table = sa.Table(
    "specializations_specialists",
    BaseModel.metadata,
    sa.Column(
        "specialization_id", sa.ForeignKey("specializations.id"), primary_key=True
    ),
    sa.Column("specialist_id", sa.ForeignKey("specialists.id"), primary_key=True),
)
