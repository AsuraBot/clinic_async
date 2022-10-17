from fastapi import APIRouter

TAG = "promotions"
PREFFIX = f"/{TAG}"


router = APIRouter(prefix=PREFFIX, tags=[TAG])


@router.get("")
async def get_promotions():
    return None


@router.get("/{name}")
async def get_promotion(name: str):
    return None
