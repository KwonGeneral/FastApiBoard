from typing import Type

from sqlalchemy.orm import Session

from follow.models import *
from follow.schemas import *

def getFollow(db: Session, follow_pk: int) -> FollowModel:
    return db.query(FollowModel).filter(FollowModel.pk == follow_pk).first()

def getFollowList(db: Session, skip: int = 0, limit: int = 100) -> list[Type[FollowModel]]:
    return db.query(FollowModel).offset(skip).limit(limit).all()

def createFollow(db: Session, follow: FollowSchema) -> FollowModel:
    db_follow = FollowModel(
        follower_pk=follow.follower_pk,
        following_pk=follow.following_pk,
    )
    db.add(db_follow)
    db.commit()
    db.refresh(db_follow)
    return db_follow

def deleteFollow(db: Session, follow_pk: int) -> FollowModel:
    follow = getFollow(db=db, follow_pk=follow_pk)
    db.delete(follow)
    db.commit()
    return follow

def updateFollow(db: Session, follow_pk: int, update_follow: FollowSchema) -> FollowModel:
    follow = getFollow(db=db, follow_pk=follow_pk)
    follow.follower_pk = update_follow.follower_pk
    follow.following_pk = update_follow.following_pk
    db.commit()
    db.refresh(follow)
    return follow