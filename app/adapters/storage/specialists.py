from typing import TYPE_CHECKING
from collections.abc import Callable
from contextlib import AbstractAsyncContextManager
from sqlalchemy import select

from app.adapters.storage.models import Specialist
from app.services.schemas.specialists import SpecialistSchema

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class SpecialistsAdapter:
    """Адаптер для доступа к данным специалистов."""

    def __init__(
        self, session_factory: Callable[[], AbstractAsyncContextManager["AsyncSession"]]
    ) -> None:
        self._session_factory = session_factory
        self._model = Specialist

    async def get_all(self, on_main: bool) -> list["SpecialistSchema"]:
        """Получить всех активных специалистов."""

        query = select(self._model).where(self._model.is_active.is_(True))

        if on_main:
            query = query.where(self._model.on_main.is_(True))

        async with self._session_factory() as session:
            rows = await session.execute(query)
            specialists = [SpecialistSchema.from_orm(row) for row in rows.scalars()]

        return specialists

    async def get(self, id: int) -> "SpecialistSchema":
        """Получить специалиста."""

        query = select(self._model).where(
            self._model.id == id, self._model.is_active.is_(True)
        )

        async with self._session_factory() as session:
            row = await session.execute(query)
            specialist = SpecialistSchema.from_orm(row.one()[0])

        return specialist
