from database import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship as relation


class User(Base):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(
        sa.String(255),
        nullable=False,
    )
    is_patrick = sa.Column(sa.Boolean)
    balance = sa.Column(sa.Integer)
    male = sa.Column(sa.Boolean, default=True)
    my_total_bill = relation("Bills", back_populates="user_bill")


class Bills(Base):
    __tablename__ = "bills"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    user_bill_id = sa.Column(sa.Integer, sa.ForeignKey("users.id"), nullable=True)
    bill_name = sa.Column(sa.String)
    bill_category = sa.Column(sa.String)
    bill_cost = sa.Column(sa.Integer)
    user_bill = relation("User", back_populates="my_total_bill")
