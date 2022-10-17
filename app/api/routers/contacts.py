from fastapi import APIRouter

TAG = "contacts"
PREFFIX = f"/{TAG}"


router = APIRouter(prefix=PREFFIX, tags=[TAG])


@router.get("")
async def get_contacts():
    return None


@router.get("/{name}")
async def get_contact(name: str):
    return None
