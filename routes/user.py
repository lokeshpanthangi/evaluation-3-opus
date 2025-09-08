from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from pydantic_schemas import User as UserSchema
from crud.user import create_user, login
from database import get_db

user_router = APIRouter()

@user_router.post("/create_user")
def create_user_endpoint(user: UserSchema, db: Session = Depends(get_db)):
    return create_user(user, db)

@user_router.post("/login")
def login_endpoint(email : str, password : str, db: Session = Depends(get_db)):
    return login(email, password, db)
