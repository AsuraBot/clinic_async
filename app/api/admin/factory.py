from fastapi import FastAPI

from app.api.admin.routes import index

PREFIX = "/admin"


def create_app(title: str, version: str) -> "FastAPI":
    """Создание подприложения."""
    app = FastAPI(title=title, version=version, docs_url=None, redoc_url=None)

    # Подключение роутеров.
    app.include_router(index.router)

    return app
