from contextlib import AbstractAsyncContextManager
from typing import TYPE_CHECKING

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Callable, Singleton

from app.adapters.storage.db import engine, session
from app.adapters.storage.specialists import SpecialistsAdapter
from app.adapters.storage.analyzes import AnalyzesAdapter
from app.adapters.storage.services import ServicesAdapter
from app.adapters.storage.contacts import ContactsAdapter
from app.settings.db import DatabaseSettings

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
    analyzes_adapter: Singleton["AnalyzesAdapter"] = Singleton(
        AnalyzesAdapter, session_factory=session_ctx.provider
    )
    services_adapter: Singleton["ServicesAdapter"] = Singleton(
        ServicesAdapter, session_factory=session_ctx.provider
    )
    contacts_adapter: Singleton["ContactsAdapter"] = Singleton(
        ContactsAdapter, session_factory=session_ctx.provider
    )


CONTAINER = Container()
