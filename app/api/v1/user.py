from fastapi import APIRouter, Depends, status, Form
from typing import Annotated, Optional
from app.schemas.user import UserCreate
from app.services.user import UserService
from app.dependency import is_admin_user, is_customer_user

user_router = APIRouter()

# register a new user
@user_router.post("/", status_code=status.HTTP_201_CREATED) 
def register_user(user_data: UserCreate):
    return UserService.register_user(user_data)

# user to login
@user_router.post("/login", status_code=status.HTTP_200_OK)
def login(name: Annotated[str, Form()], password: Annotated[str, Form()]):
    return UserService.login(name, password)

# get all users by admin
@user_router.get("/")
def get_all_users(name: Optional[str] = None, current_user: int = Depends(is_admin_user)):
    return UserService.get_all_users(name)

# get user by id
@user_router.get("/{id}")
def get_user_by_id(id: int, current_user: int = Depends(is_admin_user)):
    return UserService.get_user_by_id(id)

