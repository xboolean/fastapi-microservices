from fastapi import APIRouter, Depends
from .models import User
from .schemas import UserCreate
from project.db.db_setup import Session, get_db
import sys    
print("In module products sys.path[0], __package__ ==", sys.path[0], __package__)

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/users", response_model=UserCreate, status_code=201)
async def ping_pong(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(username=user.username, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user