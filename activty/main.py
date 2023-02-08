from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import base_result
from app.database import get_db
from app.models import ResponseData
from activty import crud
from activty.schemas import *

activity_router = APIRouter(
    prefix="/activity",
    tags=["activity"],
    responses={404: {"description": "Not found"}},
)

@activity_router.get("/", response_model=ResponseData, description="전체 활동 조회", summary="전체 활동 조회")
async def readActivityList(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return base_result.success(crud.getActivityList(db, skip=skip, limit=limit))

@activity_router.get("/{activity_pk}", response_model=ResponseData, description="특정 활동 조회", summary="특정 활동 조회")
async def readActivity(activity_pk: int, db: Session = Depends(get_db)):
    db_activity = crud.getActivity(db, activity_pk=activity_pk)
    if db_activity is None:
        return base_result.not_found()
    return base_result.success(db_activity)

@activity_router.post("/", response_model=ResponseData, description="활동 생성", summary="활동 생성")
async def createActivity(activity: ActivitySchema, db: Session = Depends(get_db)):
    return base_result.success(crud.createActivity(db=db, activity=activity))

@activity_router.put("/{activity_pk}", response_model=ResponseData, description="활동 수정", summary="활동 수정")
async def updateActivity(activity_pk: int, update_activity: ActivitySchema, db: Session = Depends(get_db)):
    db_activity = crud.getActivity(db, activity_pk=activity_pk)
    if db_activity is None:
        return base_result.not_found()
    return base_result.success(crud.updateActivity(db=db, activity_pk=activity_pk, update_activity=update_activity))

@activity_router.delete("/{activity_pk}", response_model=ResponseData, description="활동 삭제", summary="활동 삭제")
async def deleteActivity(activity_pk: int, db: Session = Depends(get_db)):
    db_activity = crud.getActivity(db, activity_pk=activity_pk)
    if db_activity is None:
        return base_result.not_found()
    return base_result.success(crud.deleteActivity(db=db, activity_pk=activity_pk))

