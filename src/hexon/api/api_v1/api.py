from fastapi import APIRouter

from hexon.api.api_v1.endpoints import hello
from hexon.api.api_v1.endpoints import flashcard

api_router = APIRouter()
api_router.include_router(hello.router, prefix="/hello", tags=["hello"])
api_router.include_router(flashcard.router, prefix="/flashcard", tags=["flashcard"])
