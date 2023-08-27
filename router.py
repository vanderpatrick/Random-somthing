from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from database import SessionLocal as Sl
import models

router = APIRouter()
db = Sl()


# serialize User model
class User(BaseModel):
    id: int
    name: str
    is_patrick: bool
    balance: int
    male: bool

    class Config:
        orm_mode = True


# serialize Bills model
class Bills(BaseModel):
    id: int
    user_bill_id: int
    bill_name: str
    bill_category: str
    bill_cost: int

    class Config:
        orm_mode = True

# Instantiate default router
@router.get("/")
def home():
    return {"welcome": "this is the homepage"}


@router.get("/users", response_model=list[User], status_code=200)
def get_user():
    user = db.query(models.User).all()
    if not user:
        raise HTTPException(status_code=404, detail="NO users found")
    return user


@router.post("/users/create", status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    # Check if the user already exists
    existing_user = db.query(models.User).filter(models.User.id == user.id).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists"
        )

    # Create a new user
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# Route to edit user in db
@router.put("/users/{user_id}", response_model=User, status_code=status.HTTP_200_OK)
def edit_user(user_id: int, user: User):
    user_to_update = db.query(models.User).filter(models.User.id == user_id).first()
    if not user_to_update:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    update_data = {
        "name": user.name,
        "is_patrick": user.is_patrick,
        "balance": user.balance,
        "male": user.male,
    }
    for field, value in update_data.items():
        setattr(user_to_update, field, value)
    db.commit()
    db.refresh(user_to_update)

    return user_to_update


# Get all bills, we might have different kinds of bill from temp to fixed bills
@router.get("/bills", response_model=list[Bills], status_code=status.HTTP_200_OK)
def get_all_bills():
    bills = db.query(models.Bills).all()
    if not bills:
        raise HTTPException(status_code=404, detail="No bills found")
    return bills


@router.post("/bills/create", status_code=status.HTTP_201_CREATED)
def create_bill(bill: Bills):
    existing_bill = db.query(models.Bills).filter(models.Bills.id == bill.id).first()
    if existing_bill:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Bill with the same ID already exists",
        )

        # Create a new bill
    new_bill = models.Bills(**bill.dict())
    db.add(new_bill)
    db.commit()
    db.refresh(new_bill)
    return new_bill


@router.put("/bills/bill_id", response_model=Bills, status_code=status.HTTP_200_OK)
def update_bill(bill: Bills, bill_id: int):
    bill_to_update = db.query(models.Bills).filter(models.Bills.id == bill_id).first()

    if not bill_to_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Bill not found")

    # Update the bill fields
    update_data = {
        "bill_name": bill.bill_name,
        "user_bill_id": bill.user_bill_id,
        "bill_category": bill.bill_category,
        "bill_cost": bill.bill_cost,
    }

    for field, value in update_data.items():
        setattr(bill_to_update, field, value)

    db.commit()
    db.refresh(bill_to_update)

    return bill_to_update
