from sqlalchemy.orm import Session

from schemas.users import UserCreate
from db.models.users import User
from core.hashing import Hasher

def create_new_user(user:UserCreate, db:Session):
    user = User(username=user.username,
            email = user.email,
            hashed_password=Hasher.get_password_hash(user.password),
            is_active=True
        )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_email(email:str, db:Session):
    user = db.query(User).filter(User.email == email).first()
    return user