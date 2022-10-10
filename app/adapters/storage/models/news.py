from datetime import date

import sqlalchemy as sa

from app.adapters.storage.db.base_model import BaseModel


class News(BaseModel):
    """Новости."""

    __tablename__ = "news"

    id: int = sa.Column(sa.BigInteger(), primary_key=True, autoincrement=True)
    title: str = sa.Column(sa.String(length=50), nullable=False)
    preview: str = sa.Column(sa.String(length=50), nullable=False)
    date: date = sa.Column(sa.Date(), nullable=False, default=date.now)
    description: str = sa.Column(sa.String(length=500), nullable=False)
    photo: str = sa.Column(sa.String(length=50), nullable=False)
