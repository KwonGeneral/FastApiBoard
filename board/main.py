from fastapi import APIRouter

board_router = APIRouter(
    prefix="/board",
    tags=["board"],
    responses={404: {"description": "Not found"}},
)