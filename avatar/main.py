from fastapi import APIRouter

avatar_router = APIRouter(
    prefix="/avatar",
    tags=["avatar"],
    responses={404: {"description": "Not found"}},
)