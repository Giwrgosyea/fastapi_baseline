from fastapi import APIRouter


from .park_router import router as park_router

router = APIRouter()
router.include_router(park_router)
