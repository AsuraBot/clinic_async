import sqlalchemy as sa
from sqlalchemy.orm import relationship

from app.adapters.storage.db.base_model import BaseModel


class Office(BaseModel):
    """Филиалы."""

    __tablename__ = "offices"

    id: int = sa.Column(sa.BigInteger(), primary_key=True, autoincrement=True)
    city_id: int = sa.Column(sa.BigInteger(), sa.ForeignKey("cities.id"))
    description: str = sa.Column(sa.String(length=100), nullable=False)
    address: str = sa.Column(sa.String(length=100), nullable=False)
    work_time: str = sa.Column(sa.String(length=100), nullable=False)
    phone: str = sa.Column(sa.String(length=20), nullable=False)
    email: str = sa.Column(sa.String(length=30), nullable=False)
    main_doctor: str = sa.Column(sa.String(length=50), nullable=False)
    main_doctor_work_time: str = sa.Column(sa.String(length=50), nullable=False)
    coor_x: str = sa.Column(sa.String(length=10), nullable=False)
    coor_y: str = sa.Column(sa.String(length=10), nullable=False)

    city: "City" = relationship("City", back_populates="offices")

    def __str__(self) -> str:
        return self.address


class City(BaseModel):
    """Города."""

    __tablename__ = "cities"

    id: int = sa.Column(sa.BigInteger(), primary_key=True, autoincrement=True)
    name: str = sa.Column(sa.String(length=30), nullable=False)

    offices: "Office" = relationship("Office", back_populates="city", uselist=True)

    def __str__(self) -> str:
        return self.name
