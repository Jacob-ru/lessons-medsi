from fastapi import FastAPI

from app.api.routes import router
from app.core import config
from pymongo import MongoClient


def init_mongo(app):
    app.mongodb_client = MongoClient(config.MONGODB_CONNECTION)
    app.database = app.mongodb_client[config.MONGODB_DB_NAME]
    print("Connected to the MongoDB database!")


def get_application() -> FastAPI:
    application: FastAPI = FastAPI(
        title=config.PROJECT_NAME,
        description=f"API сервиса {config.PROJECT_NAME}",
        root_path=config.API_ROOT_PATH,
        version=config.VERSION,
        debug=config.DEBUG,
    )

    @application.on_event("startup")
    def startup_db_client():
        init_mongo(app)

    @application.on_event("shutdown")
    def shutdown_db_client():
        app.mongodb_client.close()

    application.include_router(
        router,
        prefix=config.API_ROUTE,
        #dependencies=[Depends(log_service_request_dependency)],
    )

    return application


app = get_application()
