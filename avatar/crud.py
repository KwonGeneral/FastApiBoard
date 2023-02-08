from typing import Type

from sqlalchemy.orm import Session

from avatar.models import *
from avatar.schemas import *

def getAvatar(db: Session, avatar_pk: int) -> AvatarModel:
    return db.query(AvatarModel).filter(AvatarModel.pk == avatar_pk).first()

def getAvatarList(db: Session, skip: int = 0, limit: int = 100) -> list[Type[AvatarModel]]:
    return db.query(AvatarModel).offset(skip).limit(limit).all()

def getAvatarByOwnerPk(db: Session, owner_pk: int) -> AvatarModel:
    return db.query(AvatarModel).filter(AvatarModel.owner_pk == owner_pk).first()

def createAvatar(db: Session, avatar: AvatarSchema) -> AvatarModel:
    db_avatar = AvatarModel(
        owner_pk=avatar.owner_pk,
        version=avatar.version,
        activity_point=avatar.activity_point,
        nick_name=avatar.nick_name,
        official=avatar.official,
        picture=avatar.picture,
        picture_type=avatar.picture_type,
    )
    db.add(db_avatar)
    db.commit()
    db.refresh(db_avatar)
    return db_avatar

def updateAvatar(db: Session, avatar_pk: int, update_avatar: AvatarSchema) -> AvatarModel:
    avatar = getAvatar(db=db, avatar_pk=avatar_pk)
    avatar.owner_pk = update_avatar.owner_pk
    avatar.version = update_avatar.version
    avatar.activity_point = update_avatar.activity_point
    avatar.nick_name = update_avatar.nick_name
    avatar.official = update_avatar.official
    avatar.picture = update_avatar.picture
    avatar.picture_type = update_avatar.picture_type
    db.commit()
    db.refresh(avatar)
    return avatar

def deleteAvatar(db: Session, avatar_pk: int) -> AvatarModel:
    avatar = getAvatar(db=db, avatar_pk=avatar_pk)
    db.delete(avatar)
    db.commit()
    return avatar

def getAvatarTag(db: Session, avatar_tag_pk: int) -> AvatarTagModel:
    return db.query(AvatarTagModel).filter(AvatarTagModel.pk == avatar_tag_pk).first()

def getAvatarTagList(db: Session, skip: int = 0, limit: int = 100) -> list[Type[AvatarTagModel]]:
    return db.query(AvatarTagModel).offset(skip).limit(limit).all()

def createAvatarTag(db: Session, avatar_tag: AvatarTagSchema) -> AvatarTagModel:
    db_avatar_tag = AvatarTagModel(
        avatar_pk=avatar_tag.avatar_pk,
        tag_pk=avatar_tag.tag_pk,
    )
    db.add(db_avatar_tag)
    db.commit()
    db.refresh(db_avatar_tag)
    return db_avatar_tag

def updateAvatarTag(db: Session, avatar_tag_pk: int, update_avatar_tag: AvatarTagSchema) -> AvatarTagModel:
    avatar_tag = getAvatarTag(db=db, avatar_tag_pk=avatar_tag_pk)
    avatar_tag.avatar_pk = update_avatar_tag.avatar_pk
    avatar_tag.tag_pk = update_avatar_tag.tag_pk
    db.commit()
    db.refresh(avatar_tag)
    return avatar_tag

def deleteAvatarTag(db: Session, avatar_tag_pk: int) -> AvatarTagModel:
    avatar_tag = getAvatarTag(db=db, avatar_tag_pk=avatar_tag_pk)
    db.delete(avatar_tag)
    db.commit()
    return avatar_tag

def getNotification(db: Session, notification_pk: int) -> NotificationModel:
    return db.query(NotificationModel).filter(NotificationModel.pk == notification_pk).first()

def getNotificationList(db: Session, skip: int = 0, limit: int = 100) -> list[Type[NotificationModel]]:
    return db.query(NotificationModel).offset(skip).limit(limit).all()

def createNotification(db: Session, notification: NotificationSchema) -> NotificationModel:
    db_notification = NotificationModel(
        sender_pk=notification.sender_pk,
        receiver_pk=notification.receiver_pk,
        version=notification.version,
        type=notification.type,
    )
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)
    return db_notification

def updateNotification(db: Session, notification_pk: int, update_notification: NotificationSchema) -> NotificationModel:
    notification = getNotification(db=db, notification_pk=notification_pk)
    notification.sender_pk = update_notification.sender_pk
    notification.receiver_pk = update_notification.receiver_pk
    notification.version = update_notification.version
    notification.type = update_notification.type
    db.commit()
    db.refresh(notification)
    return notification

def deleteNotification(db: Session, notification_pk: int) -> NotificationModel:
    notification = getNotification(db=db, notification_pk=notification_pk)
    db.delete(notification)
    db.commit()
    return notification