"""office3

Revision ID: 2f0eaea88e68
Revises: 4a7cdbf0969f
Create Date: 2022-12-25 15:35:43.753645

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "2f0eaea88e68"
down_revision = "4a7cdbf0969f"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "offices",
        sa.Column("coor_x", sa.String(length=10), server_default="0", nullable=False),
    )
    op.add_column(
        "offices",
        sa.Column("coor_y", sa.String(length=10), server_default="0", nullable=False),
    )
    op.drop_column("offices", "map_code")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "offices",
        sa.Column(
            "map_code", sa.VARCHAR(length=1500), autoincrement=False, nullable=True
        ),
    )
    op.drop_column("offices", "coor_y")
    op.drop_column("offices", "coor_x")
    # ### end Alembic commands ###
