from fastapi import APIRouter

banner_router = APIRouter(
    prefix="/banner",
    tags=["banner"],
    responses={404: {"description": "Not found"}},
)