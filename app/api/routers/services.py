from fastapi import APIRouter

TAG = "services"
PREFFIX = f"/{TAG}"


router = APIRouter(prefix=PREFFIX, tags=[TAG])


@router.get("")
async def get_services():
    return None


@router.get("/{name}")
async def get_service(name: str):
    return None
