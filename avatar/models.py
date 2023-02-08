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

    owner = relationship("UserModel", foreign_keys=[owner_pk], back_populates="avatar")
    avatar_tag = relationship("AvatarTagModel", back_populates="avatar")
    follow_follower = relationship("FollowModel", foreign_keys="FollowModel.follower_pk", back_populates="avatar_follower")
    follow_following = relationship("FollowModel", foreign_keys="FollowModel.following_pk", back_populates="avatar_following")
    notification_sender = relationship("NotificationModel", foreign_keys="NotificationModel.sender_pk", back_populates="avatar_sender")
    notification_receiver = relationship("NotificationModel", foreign_keys="NotificationModel.receiver_pk", back_populates="avatar_receiver")
    activity = relationship("ActivityModel", back_populates="avatar")
    board_owner = relationship("BoardModel", foreign_keys="BoardModel.owner_pk", back_populates="owner")
    board_last_editor = relationship("BoardModel", foreign_keys="BoardModel.last_editor_pk", back_populates="last_editor")
    content_owner = relationship("ContentModel", foreign_keys="ContentModel.owner_pk", back_populates="owner")
    content_last_editor = relationship("ContentModel", foreign_keys="ContentModel.last_editor_pk", back_populates="last_editor")
    content_vote = relationship("ContentVoteModel", foreign_keys="ContentVoteModel.owner_pk", back_populates="owner")
    scrap = relationship("ScrapModel", foreign_keys="ScrapModel.owner_pk", back_populates="owner")
    change_log = relationship("ChangeLogModel", foreign_keys="ChangeLogModel.avatar_pk", back_populates="avatar")
    opinion = relationship("OpinionModel", foreign_keys="OpinionModel.owner_pk", back_populates="owner")

class AvatarTagModel(Base):
    __tablename__ = "avatar_tag"
    pk = Column(Integer, primary_key=True, index=True)
    avatar_pk = Column(Integer, ForeignKey("avatar.pk"), nullable=False)
    tag_pk = Column(Integer, ForeignKey("tag.pk"), nullable=False)

    avatar = relationship("AvatarModel", foreign_keys=[avatar_pk], back_populates="avatar_tag")
    tag = relationship("TagModel", foreign_keys=[tag_pk], back_populates="avatar_tag")

class NotificationModel(Base):
    __tablename__ = "notification"
    pk = Column(Integer, primary_key=True, index=True)
    sender_pk = Column(Integer, ForeignKey("avatar.pk"), nullable=False)
    receiver_pk = Column(Integer, ForeignKey("avatar.pk"), nullable=False)
    version = Column(String, index=True, nullable=False)
    date_created = Column(DateTime, default=datetime.datetime.utcnow, index=True, nullable=False)
    last_updated = Column(DateTime, default=datetime.datetime.utcnow, index=True, nullable=False)
    type = Column(String, index=True, nullable=False)

    avatar_sender = relationship("AvatarModel", foreign_keys=[sender_pk], back_populates="notification_sender")
    avatar_receiver = relationship("AvatarModel", foreign_keys=[receiver_pk], back_populates="notification_receiver")