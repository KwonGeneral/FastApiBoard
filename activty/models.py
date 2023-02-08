import datetime
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

class ActivityModel(Base):
    __tablename__ = "activity"
    pk = Column(Integer, primary_key=True, index=True)
    avatar_pk = Column(Integer, ForeignKey("avatar.pk"), nullable=False)
    board_pk = Column(Integer, ForeignKey("board.pk"), nullable=False)
    content_pk = Column(Integer, ForeignKey("content.pk"), nullable=False)
    version = Column(String, index=True, nullable=False)
    date_created = Column(DateTime, default=datetime.datetime.utcnow, index=True, nullable=False)
    last_updated = Column(DateTime, default=datetime.datetime.utcnow, index=True, nullable=False)
    point = Column(Integer, index=True, nullable=False)
    point_type = Column(String, index=True, nullable=False)
    type = Column(String, index=True, nullable=False)

    avatar = relationship("AvatarModel", foreign_keys=[avatar_pk], back_populates="activity")
    board = relationship("BoardModel", foreign_keys=[board_pk], back_populates="activity")
    content = relationship("ContentModel", foreign_keys=[content_pk], back_populates="activity")