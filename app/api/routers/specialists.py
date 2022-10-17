from fastapi import APIRouter

TAG = "specialists"
PREFFIX = f"/{TAG}"


router = APIRouter(prefix=PREFFIX, tags=[TAG])


@router.get("")
async def get_specialists():
    return None


@router.get("/{name}")
async def get_specialist(name: str):
    return None
