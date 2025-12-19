from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.dependencies import get_db, get_current_user
from app.database import models, schemas
from app.utils.permissions import allow_roles

router = APIRouter()

@router.get("/me", response_model=schemas.UserOut)
def me(current=Depends(get_current_user), db: Session = Depends(get_db)):
    return db.query(models.User).filter(models.User.id == current["id"]).first()

@router.get("/")
def all_users(current=Depends(get_current_user), db: Session = Depends(get_db)):
    allow_roles("admin")(current["role"])
    return db.query(models.User).all()