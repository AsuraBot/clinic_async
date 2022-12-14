from typing import TYPE_CHECKING
from app.services.exceptions import NotFoundError
from fastapi.responses import JSONResponse
from fastapi import status

if TYPE_CHECKING:
    from fastapi import FastAPI, Request


def add_all(app: "FastAPI") -> None:
    """Добавить обработчики ошибок к приложению."""

    app.add_exception_handler(NotFoundError, _not_found_error_handler)

    return


async def _not_found_error_handler(
    _request: "Request", exception: "Exception"
) -> "JSONResponse":
    """Обработчик ошибок 404."""

    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND, content={"message": "object not found."}
    )
