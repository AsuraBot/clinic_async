import sqlalchemy as sa
from app.adapters.storage.models.base import BaseModel


class ServiceType(BaseModel):
    """Тип услуг."""

    __tablename__ = "services_types"

    id: int = sa.Column(sa.BigInteger(), primary_key=True, autoincrement=True)
    name: str = sa.Column(sa.String(length=30), nullable=False)
    on_main: bool = sa.Column(sa.Boolean(), default=False)


class Service(BaseModel):
    """Услуги."""

    __tablename__ = "services"

    id: int = sa.Column(sa.BigInteger(), primary_key=True, autoincrement=True)
    service_type_id: int = sa.Column(
        sa.BigInteger(), sa.ForeignKey("services_types.id")
    )
    name: str = sa.Column(sa.String(length=30), nullable=False)
    is_active: bool = sa.Column(sa.Boolean(), default=False)
    on_main: bool = sa.Column(sa.Boolean(), default=False)
