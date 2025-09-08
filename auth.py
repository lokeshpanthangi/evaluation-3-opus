from jose import jwt, JWTError
from datetime import datetime, timedelta
from passlib.context import CryptContext
from dotenv import load_dotenv
import os
load_dotenv()

# Secret key and algorithm for JWT
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict):
    payload = {
        "_id" : data.get("_id"),
        "email": data.get("email"),
        "user_type": data.get("user_type"),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)