from sqlalchemy.orm import Session
from models import UserModel
from schemas import UserCreate

def get_user(db: Session, user_id: int):
    return db.query(UserModel).filter(UserModel.id == user_id).first()

def create_user(db: Session, user: UserCreate):
    db_user = UserModel(id=user.id, fio=user.fio)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, new_data: UserCreate):
    db_user = get_user(db, user_id)
    if not db_user:
        return None
    db_user.fio = new_data.fio
    db.commit()
    db.refresh(db_user)

def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    if not db_user:
        return None
    db.delete(db_user)
    db.commit()
    return db_user
