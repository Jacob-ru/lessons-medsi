from pydantic import BaseModel


class User(BaseModel):
    username: str
    fio: str
    password_hash: str


