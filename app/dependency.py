from fastapi import HTTPException, status
from app.schemas.user import User, UserRole
from app.services.user import UserService


def is_admin_user(user_id: int):
    user: User = UserService.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail= "User cannot be found")
    
    if user.role != UserRole.admin:
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail= "Sorry! You do not have permission to perform this action")
    
def is_customer_user(user_id: int):
    user: User = UserService.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User cannot be found")
    
    if user.role != UserRole.customer:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= "Sorry! You do not have permission to perform this action")