from typing import Type

from sqlalchemy.orm import Session

from activty.models import *
from activty.schemas import *

def getActivity(db: Session, activity_pk: int) -> ActivityModel:
    return db.query(ActivityModel).filter(ActivityModel.pk == activity_pk).first()

def getActivityList(db: Session, skip: int = 0, limit: int = 100) -> list[Type[ActivityModel]]:
    return db.query(ActivityModel).offset(skip).limit(limit).all()

def createActivity(db: Session, activity: ActivitySchema) -> ActivityModel:
    db_activity = ActivityModel(
        avatar_pk=activity.avatar_pk,
        board_pk=activity.board_pk,
        content_pk=activity.content_pk,
        version=activity.version,
        point=activity.point,
        point_type=activity.point_type,
        type=activity.type,
    )
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity

def updateActivity(db: Session, activity_pk: int, update_activity: ActivitySchema) -> ActivityModel:
    activity = getActivity(db=db, activity_pk=activity_pk)
    activity.avatar_pk = update_activity.avatar_pk
    activity.board_pk = update_activity.board_pk
    activity.content_pk = update_activity.content_pk
    activity.version = update_activity.version
    activity.point = update_activity.point
    activity.point_type = update_activity.point_type
    activity.type = update_activity.type
    db.commit()
    db.refresh(activity)
    return activity

def deleteActivity(db: Session, activity_pk: int) -> ActivityModel:
    activity = getActivity(db=db, activity_pk=activity_pk)
    db.delete(activity)
    db.commit()
    return activity