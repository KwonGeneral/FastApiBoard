from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import base_result
from app.database import get_db
from app.models import ResponseData
from avatar import crud
from avatar.schemas import *

avatar_router = APIRouter(
    prefix="/avatar",
    tags=["avatar"],
    responses={404: {"description": "Not found"}},
)

@avatar_router.get("/", response_model=ResponseData, description="전체 아바타 조회", summary="전체 아바타 조회")
async def readAvatarList(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_avatar_list = crud.getAvatarList(db, skip=skip, limit=limit)
    return base_result.success(db_avatar_list)

@avatar_router.get("/{avatar_pk}", response_model=ResponseData, description="특정 아바타 조회", summary="특정 아바타 조회")
async def readAvatar(avatar_pk: int, db: Session = Depends(get_db)):
    db_avatar = crud.getAvatar(db, avatar_pk=avatar_pk)
    if db_avatar is None:
        return base_result.not_found()
    return base_result.success(db_avatar)

@avatar_router.post("/", response_model=ResponseData, description="아바타 생성", summary="아바타 생성")
async def createAvatar(avatar: AvatarSchema, db: Session = Depends(get_db)):
    db_avatar = crud.getAvatarByOwnerPk(db, owner_pk=avatar.owner_pk)
    if db_avatar is not None:
        return base_result.not_found()
    return base_result.success(crud.createAvatar(db, avatar))

@avatar_router.put("/{avatar_pk}", response_model=ResponseData, description="아바타 수정", summary="아바타 수정")
async def updateAvatar(avatar_pk: int, update_avatar: AvatarSchema, db: Session = Depends(get_db)):
    db_avatar = crud.getAvatar(db, avatar_pk=avatar_pk)
    if db_avatar is None:
        return base_result.not_found()
    return base_result.success(crud.updateAvatar(db, avatar_pk, update_avatar))

@avatar_router.delete("/{avatar_pk}", response_model=ResponseData, description="아바타 삭제", summary="아바타 삭제")
async def deleteAvatar(avatar_pk: int, db: Session = Depends(get_db)):
    db_avatar = crud.getAvatar(db, avatar_pk=avatar_pk)
    if db_avatar is None:
        return base_result.not_found()
    return base_result.success(crud.deleteAvatar(db, avatar_pk))

@avatar_router.get("/tag/", response_model=ResponseData, description="아바타 태그 조회", summary="아바타 태그 조회")
async def readAvatarTagList(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_avatar_tag_list = crud.getAvatarTagList(db, skip=skip, limit=limit)
    return base_result.success(db_avatar_tag_list)

@avatar_router.get("/tag/{avatar_tag_pk}", response_model=ResponseData, description="특정 아바타 태그 조회", summary="특정 아바타 태그 조회")
async def readAvatarTag(avatar_tag_pk: int, db: Session = Depends(get_db)):
    db_avatar_tag = crud.getAvatarTag(db, avatar_tag_pk=avatar_tag_pk)
    if db_avatar_tag is None:
        return base_result.not_found()
    return base_result.success(db_avatar_tag)

@avatar_router.post("/tag/", response_model=ResponseData, description="아바타 태그 생성", summary="아바타 태그 생성")
async def createAvatarTag(avatar_tag: AvatarTagSchema, db: Session = Depends(get_db)):
    return base_result.success(crud.createAvatarTag(db, avatar_tag))

@avatar_router.put("/tag/{avatar_tag_pk}", response_model=ResponseData, description="아바타 태그 수정", summary="아바타 태그 수정")
async def updateAvatarTag(avatar_tag_pk: int, update_avatar_tag: AvatarTagSchema, db: Session = Depends(get_db)):
    db_avatar_tag = crud.getAvatarTag(db, avatar_tag_pk=avatar_tag_pk)
    if db_avatar_tag is None:
        return base_result.not_found()
    return base_result.success(crud.updateAvatarTag(db, avatar_tag_pk, update_avatar_tag))

@avatar_router.delete("/tag/{avatar_tag_pk}", response_model=ResponseData, description="아바타 태그 삭제", summary="아바타 태그 삭제")
async def deleteAvatarTag(avatar_tag_pk: int, db: Session = Depends(get_db)):
    db_avatar_tag = crud.getAvatarTag(db, avatar_tag_pk=avatar_tag_pk)
    if db_avatar_tag is None:
        return base_result.not_found()
    return base_result.success(crud.deleteAvatarTag(db, avatar_tag_pk))

@avatar_router.get("/notification/", response_model=ResponseData, description="아바타 알림 조회", summary="아바타 알림 조회")
async def readNotificationList(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_avatar_notification_list = crud.getNotificationList(db, skip=skip, limit=limit)
    return base_result.success(db_avatar_notification_list)

@avatar_router.get("/notification/{notification_pk}", response_model=ResponseData, description="특정 아바타 알림 조회", summary="특정 아바타 알림 조회")
async def readNotification(notification_pk: int, db: Session = Depends(get_db)):
    db_avatar_notification = crud.getNotification(db, notification_pk=notification_pk)
    if db_avatar_notification is None:
        return base_result.not_found()
    return base_result.success(db_avatar_notification)

@avatar_router.post("/notification/", response_model=ResponseData, description="아바타 알림 생성", summary="아바타 알림 생성")
async def createNotification(notification: NotificationSchema, db: Session = Depends(get_db)):
    return base_result.success(crud.createNotification(db, notification))

@avatar_router.put("/notification/{notification_pk}", response_model=ResponseData, description="아바타 알림 수정", summary="아바타 알림 수정")
async def updateNotification(notification_pk: int, update_notification: NotificationSchema, db: Session = Depends(get_db)):
    db_avatar_notification = crud.getNotification(db, notification_pk=notification_pk)
    if db_avatar_notification is None:
        return base_result.not_found()
    return base_result.success(crud.updateNotification(db, notification_pk, update_notification))

@avatar_router.delete("/notification/{notification_pk}", response_model=ResponseData, description="아바타 알림 삭제", summary="아바타 알림 삭제")
async def deleteNotification(notification_pk: int, db: Session = Depends(get_db)):
    db_avatar_notification = crud.getNotification(db, notification_pk=notification_pk)
    if db_avatar_notification is None:
        return base_result.not_found()
    return base_result.success(crud.deleteNotification(db, notification_pk))