from fastapi import APIRouter

area_router = APIRouter(
    prefix="/area",
    tags=["area"],
    responses={404: {"description": "Not found"}},
)