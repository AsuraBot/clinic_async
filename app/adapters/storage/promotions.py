from collections.abc import Callable
from contextlib import AbstractAsyncContextManager
from typing import TYPE_CHECKING

from sqlalchemy import select
from sqlalchemy.exc import NoResultFound

from app.adapters.storage.models import Promotion
from app.services.schemas.promotions import PromotionSchema
from app.services.exceptions import NotFoundError

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class PromotionsAdapter:
    """Адаптер для доступа к данным акций."""

    def __init__(
        self, session_factory: Callable[[], AbstractAsyncContextManager["AsyncSession"]]
    ) -> None:
        self._session_factory = session_factory
        self._model = Promotion

    async def get_all(self, on_main: bool) -> list["PromotionSchema"]:
        """Получить все активные акции."""

        query = select(self._model).where(self._model.is_active.is_(True))

        if on_main:
            query = query.where(self._model.on_main.is_(True))

        async with self._session_factory() as session:
            rows = await session.execute(query)
            promotions = [PromotionSchema.from_orm(row) for row in rows.scalars()]

        return promotions

    async def get(self, id: int) -> "PromotionSchema":
        """Получить акцию."""

        query = select(self._model).where(
            self._model.id == id, self._model.is_active.is_(True)
        )

        async with self._session_factory() as session:
            row = await session.execute(query)

            try:
                promotion = PromotionSchema.from_orm(row.one()[0])
            except NoResultFound:
                raise NotFoundError(f"Акция с {id=} не найдена.")

        return promotion
