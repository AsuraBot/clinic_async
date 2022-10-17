from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Singleton, Callable
from app.settings.db import DatabaseSettings
from contextlib import AbstractAsyncContextManager
from app.adapters.storage.db import engine, session
from typing import TYPE_CHECKING

from app.adapters.storage.specialists import SpecialistsAdapter

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession


class Container(DeclarativeContainer):
    """Контейнер зависимостей приложения."""

    db_settings: Singleton["DatabaseSettings"] = Singleton(DatabaseSettings)

    async_engine: Singleton["AsyncEngine"] = Singleton(engine.get_async)
    session_ctx: Callable[AbstractAsyncContextManager["AsyncSession"]] = Callable(
        session.get_context, engine=async_engine.provided
    )

    specialists_adapter: Singleton["SpecialistsAdapter"] = Singleton(
        SpecialistsAdapter, session_factory=session_ctx.provider
    )


CONTAINER = Container()
