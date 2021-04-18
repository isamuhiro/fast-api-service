from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.database import SessionLocal
from schemas.user import UserSchema
from services.user import get_users, create_user


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter(prefix="/user", tags=["users"])


@router.get("/")
def all(db: Session = Depends(get_db)):
    return get_users(db)


@router.get("/{user_id}")
def find_by_id(user_id: int, db: Session = Depends(get_db)):
    # TODO: Implement
    pass


@router.post('/')
def create(user: UserSchema, db: Session = Depends(get_db)):
    return create_user(user, db)
