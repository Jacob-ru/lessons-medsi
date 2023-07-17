import pytest


@pytest.fixture(autouse=True)
def prepare_db():
    """Подготовка базы для использования в тестах"""
    from app.main import app
    from app.main import init_mongo
    init_mongo(app, db_prefix="test_")
    yield
    app.database['orders'].drop()
