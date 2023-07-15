from fastapi import Depends, HTTPException
from jose import JWTError
from starlette import status

from app.models.domain import User
from app.services.auth import UserNotFound, get_user_from_jwt_token, oauth2_scheme



async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    """Зависимость определяющая пользователя на основе jwt токена переданного в запросе"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        user = get_user_from_jwt_token(token)
    except (JWTError, UserNotFound):
        raise credentials_exception
    if user is None:
        raise credentials_exception
    return user
