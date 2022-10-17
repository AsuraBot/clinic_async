from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Singleton, Callable
from app.settings.db import DatabaseSettings
from contextlib import AbstractAsyncContextManager
from app.adapters.storage.db import engine
from typing import TYPE_CHECKING, Callable

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession


class Container(DeclarativeContainer):
    """Контейнер зависимостей приложения."""

    db_settings: Singleton["DatabaseSettings"] = Singleton(DatabaseSettings)

    async_engine: Singleton["AsyncEngine"] = Singleton(engine.get_async)
    session_ctx: Callable[AbstractAsyncContextManager["AsyncSession"]] = Callable(
        session.context, engine=async_engine.provided
    )
