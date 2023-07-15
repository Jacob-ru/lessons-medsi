import datetime as dt

from fastapi import Depends, HTTPException, status, Form

from app.api.dependencies.security import get_current_user
from app.core import config
from app.models.domain.user import User
from app.models.schemas.user import PublicUserInfo, UserLogin, Token
from app.services.auth import authenticate_user, create_access_token
from .routes import router


@router.post("/token", response_model=Token)
async def login_for_access_token(
    username: str = Form(...),
    password: str = Form(...),
):
    user = authenticate_user(username, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = dt.timedelta(minutes=config.JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type='bearer')


@router.get("/me", response_model=PublicUserInfo)
def get_current_user_info(user: User=Depends(get_current_user)):
    return user