import sqlalchemy as sa

from app.adapters.storage.db.base_model import BaseModel


class Page(BaseModel):
    """Статические страницы."""

    __tablename__ = "pages"

    id: int = sa.Column(sa.BigInteger(), primary_key=True, autoincrement=True)
    url: str = sa.Column(sa.String(length=100), nullable=False)
    title: str = sa.Column(sa.String(length=20), nullable=False)
    body: str = sa.Column(sa.Text(), nullable=False)
    is_active: bool = sa.Column(sa.Boolean(), default=False)
