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

    class Config:
        orm_mode = True


# serialize Bills model

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
def create_user(user: User)-> dict:
    existing_user = db.query(models.User).filter(models.User.id == user.id).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists"
        )
    # create new user
    new_user = models.User(**user.dict(exclude={"id"}))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
# Route to edit user in db
# @router.put("/users/{user_id}", response_model=User, status_code=status.HTTP_200_OK)
# def edit_user(user_id: int, user: User):
#     user_to_update = db.query(models.User).filter(models.User.id == user_id).first()
#     if not user_to_update:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
#         )
#     update_data = {
#         "name": user.name,
#         "is_patrick": user.is_patrick,
#         "balance": user.balance,
#         "male": user.male,
#     }
#     for field, value in update_data.items():
#         setattr(user_to_update, field, value)
#     db.commit()
#     db.refresh(user_to_update)
#
#     return user_to_update



#
# @router.delete('/user/{user_id', response_model=User, status_code=status.HTTP_200_OK)
# def delete_user(user_id: int):
#     user_to_be_deleted = db.query(models.User).filter(models.User.id == user_id).first()
#     if not user_to_be_deleted:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
#
#     db.delete(user_to_be_deleted)
#     db.commit()
#
#     return user_to_be_deleted
