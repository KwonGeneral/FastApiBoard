from fastapi import APIRouter

follow_router = APIRouter(
    prefix="/follow",
    tags=["follow"],
    responses={404: {"description": "Not found"}},
)