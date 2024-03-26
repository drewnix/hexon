from fastapi import APIRouter

from hexon.api.api_v1.endpoints import cards, hello, login, users

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(hello.router, prefix="/hello", tags=["hello"])
api_router.include_router(cards.router, prefix="/card", tags=["cards"])
