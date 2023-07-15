from pydantic import BaseModel

class PublicUserInfo(BaseModel):
    username: str
    fio: str


class UserLogin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str
