from fastapi import APIRouter

TAG = "pages"
PREFFIX = f"/{TAG}"


router = APIRouter(prefix=PREFFIX, tags=[TAG])


@router.get("")
async def get_pages():
    return None


@router.get("/{name}")
async def get_page(name: str):
    return None
