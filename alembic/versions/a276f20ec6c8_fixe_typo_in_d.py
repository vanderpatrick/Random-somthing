"""Fixe typo in d

Revision ID: a276f20ec6c8
Revises: c7b1c570525c
Create Date: 2023-09-03 14:44:39.091258

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a276f20ec6c8'
down_revision: Union[str, None] = 'c7b1c570525c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
