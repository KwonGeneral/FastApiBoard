import datetime
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base


class AvatarModel(Base):
    __tablename__ = "avatar"
    pk = Column(Integer, primary_key=True, index=True)
    owner_pk = Column(Integer, ForeignKey("user.pk"), nullable=False)
    version = Column(String, index=True, nullable=False)
    activity_point = Column(Integer, index=True, nullable=False)
    nick_name = Column(String, index=True, nullable=False)
    official = Column(Boolean, default=False, index=True, nullable=True)
    picture = Column(String, index=True, nullable=False)
    picture_type = Column(Integer, index=True, nullable=False)

    owner = relationship("UserModel", back_populates="avatar")
    avatar_tag = relationship("AvatarTagModel", back_populates="avatar")
    follower = relationship("FollowModel", back_populates="follower")
    following = relationship("FollowModel", back_populates="following")
    sender = relationship("NotificationModel", back_populates="sender")
    receiver = relationship("NotificationModel", back_populates="receiver")
    activity = relationship("ActivityModel", back_populates="avatar")

class AvatarTagModel(Base):
    __tablename__ = "avatar_tag"
    pk = Column(Integer, primary_key=True, index=True)
    avatar_pk = Column(Integer, ForeignKey("avatar.pk"), nullable=False)
    tag_pk = Column(Integer, ForeignKey("tag.pk"), nullable=False)

    avatar = relationship("AvatarModel", back_populates="avatar_tag")
    tag = relationship("TagModel", back_populates="avatar_tag")

class NotificationModel(Base):
    __tablename__ = "notification"
    pk = Column(Integer, primary_key=True, index=True)
    sender_pk = Column(Integer, ForeignKey("avatar.pk"), nullable=False)
    receiver_pk = Column(Integer, ForeignKey("avatar.pk"), nullable=False)
    version = Column(String, index=True, nullable=False)
    date_created = Column(DateTime, default=datetime.datetime.utcnow, index=True, nullable=False)
    last_updated = Column(DateTime, default=datetime.datetime.utcnow, index=True, nullable=False)
    type = Column(String, index=True, nullable=False)

    sender = relationship("AvatarModel", back_populates="notification")
    receiver = relationship("AvatarModel", back_populates="notification")