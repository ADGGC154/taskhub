from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.db.session import get_db
from app.models.user import User
from app.schemas.user import UserOut, UserRegister

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register(payload: UserRegister, db: Session = Depends(get_db)):
    # 检查邮箱是否已存在
    if db.query(User).filter(User.email == payload.email).first():
        raise HTTPException(status_code=400, detail="邮箱已被注册")

    # 检查用户名是否已存在
    if db.query(User).filter(User.username == payload.username).first():
        raise HTTPException(status_code=400, detail="用户名已被占用")

    user = User(
        email=payload.email,
        username=payload.username,
        hashed_password=hash_password(payload.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user