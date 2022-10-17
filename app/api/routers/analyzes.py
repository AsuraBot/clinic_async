from fastapi import APIRouter

TAG = "analyzes"
PREFFIX = f"/{TAG}"


router = APIRouter(prefix=PREFFIX, tags=[TAG])


@router.get("")
async def get_analyzes():
    return None


@router.get("/{name}")
async def get_analysis(name: str):
    return None
