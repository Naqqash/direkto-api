# routes/users.py
from fastapi import APIRouter, HTTPException, Depends, status
from datetime import timedelta
from sqlalchemy.orm import Session
from uuid import UUID
from app.api.dependencies import dependencies
from app.api.auth import authentication
from app.api.models import models
from app.api.schemas import schemas
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter()


@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(dependencies.get_db)):
    # Verify that the two passwords match
    if user.password != user.password_confirmation:
        raise HTTPException(status_code=400, detail="Passwords do not match")
    hashed_password = authentication.get_password_hash(user.password)
    db_user = models.User(
        # id=user.id,
        name=user.name,
        email=user.email,
        hashed_password=hashed_password,
        is_admin=user.is_admin,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/{user_id}", response_model=schemas.User)
def read_user(user_id: UUID, db: Session = Depends(dependencies.get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/", response_model=list[schemas.User])
def read_users(
    skip: int = 0, limit: int = 10, db: Session = Depends(dependencies.get_db)
):
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users


@router.put("/{user_id}", response_model=schemas.User)
def update_user(
    user_id: UUID, user: schemas.UserUpdate, db: Session = Depends(dependencies.get_db)
):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    for var, value in vars(user).items():
        setattr(db_user, var, value) if value else None
    db.commit()
    db.refresh(db_user)
    return db_user


@router.delete("/{user_id}")
def delete_user(user_id: UUID, db: Session = Depends(dependencies.get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return {"ok": True}


@router.post("/signup", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(dependencies.get_db)):
    if user.password != user.password_confirmation:
        raise HTTPException(status_code=400, detail="Passwords do not match")
    hashed_password = authentication.get_password_hash(user.password)
    db_user = models.User(
        name=user.name,
        email=user.email,
        hashed_password=hashed_password,
        is_admin=user.is_admin,  # Assuming you want to include this, otherwise remove it
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
