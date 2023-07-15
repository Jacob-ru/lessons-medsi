import datetime as dt

from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from passlib.context import CryptContext

from app.core import config
from app.db.repositories import UsersRepo
from app.db.repositories.users import UsersRepo

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="v1/token")


def verify_password(plain_password, hashed_password):
    """Проверка соответствия переданного пароля хешированного значению пароля пользователя"""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    """Получение хешированного значения пароля для сохранения в БД"""
    return pwd_context.hash(password)


def authenticate_user(username: str, password: str):
    """Проверка логика и пароль пользователя"""
    user = UsersRepo.get_user(username)
    if not user:
        return False
    if not verify_password(password, user.password_hash):
        return False
    return user


def create_access_token(data: dict, expires_delta: dt.timedelta | None = None):
    """Создание jwt токена с заданным содержимым"""
    to_encode = data.copy()
    if expires_delta:
        expire = dt.datetime.utcnow() + expires_delta
    else:
        expire = dt.datetime.utcnow() + dt.timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, config.SECRET_KEY, algorithm=config.JWT_ALGORITHM)
    return encoded_jwt


class UserNotFound(Exception):
    pass


def get_user_from_jwt_token(token: str):
    """Получение юзера на основе токена"""
    payload = jwt.decode(token, config.SECRET_KEY, algorithms=[config.JWT_ALGORITHM])
    username: str = payload.get("sub")
    if username is None:
        raise UserNotFound
    user = UsersRepo.get_user(username)
    return user
