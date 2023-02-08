import datetime
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

class FollowModel(Base):
    __tablename__ = "follow"
    pk = Column(Integer, primary_key=True, index=True)
    follower_pk = Column(Integer, ForeignKey("avatar.pk"), nullable=False)
    following_pk = Column(Integer, ForeignKey("avatar.pk"), nullable=False)
    date_created = Column(DateTime, default=datetime.datetime.utcnow, index=True, nullable=False)

    avatar_follower = relationship("AvatarModel", foreign_keys=[follower_pk], back_populates="follow_follower")
    avatar_following = relationship("AvatarModel", foreign_keys=[following_pk], back_populates="follow_following")