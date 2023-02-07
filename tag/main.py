from fastapi import APIRouter

tag_router = APIRouter(
    prefix="/tag",
    tags=["tag"],
    responses={404: {"description": "Not found"}},
)