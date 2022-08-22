from fastapi import FastAPI


def create_app() -> "FastAPI":
    """Создать приложение FastAPI."""
    app = FastAPI(title="clinic", version="0.1.0", redoc_url=None)
    return app
