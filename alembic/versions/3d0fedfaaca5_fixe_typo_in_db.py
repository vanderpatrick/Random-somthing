"""Fixe typo in db

Revision ID: 3d0fedfaaca5
Revises: 24f3d13aa4df
Create Date: 2023-08-27 17:24:04.578080

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "3d0fedfaaca5"
down_revision: Union[str, None] = "24f3d13aa4df"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("bills", sa.Column("bill_cost", sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("bills", "bill_cost")
    # ### end Alembic commands ###
