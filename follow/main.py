from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import base_result
from app.database import get_db
from app.models import ResponseData
from follow import crud
from follow.schemas import *

follow_router = APIRouter(
    prefix="/follow",
    tags=["follow"],
    responses={404: {"description": "Not found"}},
)

@follow_router.get("/", response_model=ResponseData, description="전체 팔로우 조회", summary="전체 팔로우 조회")
async def readFollowList(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    follow_list = crud.getFollowList(db, skip=skip, limit=limit)
    return base_result.success(follow_list)

@follow_router.get("/{follow_pk}", response_model=ResponseData, description="특정 팔로우 조회", summary="특정 팔로우 조회")
async def readFollow(follow_pk: int, db: Session = Depends(get_db)):
    db_follow = crud.getFollow(db, follow_pk=follow_pk)
    if db_follow is None:
        return base_result.not_found()
    return base_result.success(db_follow)

@follow_router.post("/", response_model=ResponseData, description="팔로우 생성", summary="팔로우 생성")
async def createFollow(follow: FollowSchema, db: Session = Depends(get_db)):
    return base_result.success(crud.createFollow(db, follow))

@follow_router.put("/{follow_pk}", response_model=ResponseData, description="팔로우 수정", summary="팔로우 수정")
async def updateFollow(follow_pk: int, update_follow: FollowSchema, db: Session = Depends(get_db)):
    db_follow = crud.getFollow(db, follow_pk=follow_pk)
    if db_follow is None:
        return base_result.not_found()
    return base_result.success(crud.updateFollow(db, follow_pk, update_follow))

@follow_router.delete("/{follow_pk}", response_model=ResponseData, description="팔로우 삭제", summary="팔로우 삭제")
async def deleteFollow(follow_pk: int, db: Session = Depends(get_db)):
    db_follow = crud.getFollow(db, follow_pk=follow_pk)
    if db_follow is None:
        return base_result.not_found()
    return base_result.success(crud.deleteFollow(db, follow_pk))