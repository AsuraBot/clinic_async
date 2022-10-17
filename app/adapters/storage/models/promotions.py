import sqlalchemy as sa

from app.adapters.storage.models.base import BaseModel


class Promotion(BaseModel):
    """Акции."""

    __tablename__ = "promotions"

    id: int = sa.Column(sa.BigInteger(), primary_key=True, autoincrement=True)
    sale: str = sa.Column(sa.String(length=30), nullable=False)
    title: str = sa.Column(sa.String(length=20), nullable=False)
    description: str = sa.Column(sa.String(length=100), nullable=False)
    photo: str = sa.Column(sa.String(length=150), nullable=True)
    services: str = sa.Column(sa.String(length=100), nullable=False)
    promotion_date: str = sa.Column(sa.String(length=100), nullable=False)
    url: str = sa.Column(sa.String(length=100), nullable=False)
    is_active: bool = sa.Column(sa.Boolean(), default=False)
    on_main: bool = sa.Column(sa.Boolean(), default=False)
