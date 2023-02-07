import datetime
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

class FollowModel(Base):
    __tablename__ = "follow"
    pk = Column(Integer, primary_key=True, index=True)
    follower_id = Column(Integer, ForeignKey("avatar.pk"), nullable=False)
    following_id = Column(Integer, ForeignKey("avatar.pk"), nullable=False)
    date_created = Column(DateTime, default=datetime.datetime.utcnow, index=True, nullable=False)

    follower = relationship("AvatarModel", back_populates="follow")
    following = relationship("AvatarModel", back_populates="follow")