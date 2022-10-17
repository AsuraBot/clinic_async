from fastapi import APIRouter

TAG = "news"
PREFFIX = f"/{TAG}"


router = APIRouter(prefix=PREFFIX, tags=[TAG])


@router.get("")
async def get_news():
    return None


@router.get("/{name}")
async def get_news(name: str):
    return None
