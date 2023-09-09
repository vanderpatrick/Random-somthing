from database import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship as relation


class User(Base):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(
        sa.String(255),
        nullable=False,
    )
    is_patrick = sa.Column(sa.Boolean)
    balance = sa.Column(sa.Integer)


