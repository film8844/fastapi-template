from fastapi import APIRouter


router = APIRouter(prefix="/api/example", tags=["Example"])


@router.get("/")
async def example():
    'example'
