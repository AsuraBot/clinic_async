import sqlalchemy as sa

from app.adapters.storage.db.base_model import BaseModel


class AnalysisType(BaseModel):
    """Тип анализов."""

    __tablename__ = "analyzes_types"

    id: int = sa.Column(sa.BigInteger(), primary_key=True, autoincrement=True)
    name: str = sa.Column(sa.String(length=30), nullable=False)
    description: str = sa.Column(sa.Text())


class Analysis(BaseModel):
    """Анализы."""

    __tablename__ = "analyzes"

    id: int = sa.Column(sa.BigInteger(), primary_key=True, autoincrement=True)
    name: str = sa.Column(sa.String(length=30), nullable=False)
    preparation: str = sa.Column(sa.Text())
    period: str = sa.Column(sa.String(length=30), nullable=False)
    is_acive: bool = sa.Column(sa.Boolean(), default=False)


analyzes_types_analyzes_table = sa.Table(
    "analyzes_types_analyzes",
    BaseModel.metadata,
    sa.Column("analysis_type_id", sa.ForeignKey("analyzes_types.id"), primary_key=True),
    sa.Column("analysis_id", sa.ForeignKey("analyzes.id"), primary_key=True),
)
