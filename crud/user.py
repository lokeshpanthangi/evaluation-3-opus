from models import User
from pydantic_schemas import User as UserSchema
from auth import create_access_token, hash_password, verify_password



def create_user(user: UserSchema, db):
    new_user = User(
        username=user.username,
        email=user.email,
        password=hash_password(user.password),
        user_type=user.user_type,
        company_name=user.company_name

    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return create_access_token(new_user)


def login(email: str, password: str, db):
    user = db.query(User).filter(User.email == email).first()
    if user and verify_password(password, user.password):
        return create_access_token(user)
    return None