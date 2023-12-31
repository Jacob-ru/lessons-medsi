from fastapi import FastAPI

from app.api.routes import router
from app.core import config


def get_application() -> FastAPI:
    application: FastAPI = FastAPI(
        title=config.PROJECT_NAME,
        description=f"API сервиса {config.PROJECT_NAME}",
        root_path=config.API_ROOT_PATH,
        version=config.VERSION,
        debug=config.DEBUG,
    )

    application.include_router(
        router,
        prefix=config.API_ROUTE,
        #dependencies=[Depends(log_service_request_dependency)],
    )

    return application


app = get_application()
