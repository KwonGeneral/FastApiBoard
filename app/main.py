import sys

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from activty.main import activity_router
from area.main import area_router
from avatar.main import avatar_router
from banner.main import banner_router
from board.main import board_router
from file.main import file_router
from follow.main import follow_router
from tag.main import tag_router
from user.main import user_router

from .database import *

sys.setrecursionlimit(10000)

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(area_router)
app.include_router(avatar_router)
app.include_router(banner_router)
app.include_router(board_router)
app.include_router(file_router)
app.include_router(follow_router)
app.include_router(tag_router)
app.include_router(user_router)

@app.get("/")
async def root():
    return {"message": "TEST API"}