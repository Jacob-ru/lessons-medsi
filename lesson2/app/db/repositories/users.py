from app.models.domain.user import User


USERS = {
    'testuser': User(username='testuser',
                     fio='ИвановИванИванович',
                     password_hash='$2b$12$VD.VbVWi/LBQoRgyPrqzWuxqYMs6Cy7mHq/hwKsESbRJXoIlU5Ad6')
}

class UsersRepo:
    @classmethod
    def get_user(cls, username: str) -> User:
        return USERS[username]
