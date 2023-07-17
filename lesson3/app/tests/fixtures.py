import pytest


@pytest.fixture(autouse=True, scope='session')
def prepare_db():
    """Подготовка базы для использования в тестах"""
    from app.main import app
    from app.main import init_mongo
    init_mongo(app, db_prefix="test_")


@pytest.fixture(autouse=True, scope='function')
def clean_db(prepare_db):
    from app.main import app
    yield
    app.database['orders'].drop()

