from fastapi import APIRouter

activity_router = APIRouter(
    prefix="/activity",
    tags=["activity"],
    responses={404: {"description": "Not found"}},
)