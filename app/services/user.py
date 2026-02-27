from fastapi import HTTPException, status
from app.schemas.user import User, UserCreate
from app.core.user import user_db
from typing import Optional

class UserService:

    @staticmethod
    def register_user(user_data: UserCreate):
        for user in user_db.values():
            if user.email == user_data.email:
                return {"message": "Email already exists"}
            
        user_id = len(user_db) + 1
        new_user: User = User(
            id = user_id,
            name = user_data.name,
            email = user_data.email,
            password = user_data.password,
            role = user_data.role
        )
        user_db[user_id] = new_user
        return new_user
    
    @staticmethod
    def login(name: str, password: str):
        # checking if user exists
        for user in user_db.values():
            if user.name == name and user.password == password:
                return {"message": "Login successful"}
            
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid name or password"
        )
    
    @staticmethod
    def get_all_users(name: Optional[str] = None):
        if not name:
            return list(user_db.values())
        
        users_list = []

        if name:
            for users in user_db.values():
                if users.name == name:
                    users_list.append(name)
        return users_list

    @staticmethod 
    def get_user_by_id(user_id: int):
        user = user_db.get(user_id)
        
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "User cannot be found")
        return user