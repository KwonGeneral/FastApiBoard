import datetime
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base


class TagModel(Base):
    __tablename__ = "tag"
    pk = Column(Integer, primary_key=True, index=True)
    date_created = Column(DateTime, default=datetime.datetime.utcnow, index=True, nullable=False)
    tagged_count = Column(Integer, default=0, index=True, nullable=False)
    name = Column(String, index=True, nullable=False)
    description = Column(String, index=True, nullable=True)

    avatar_tag = relationship("AvatarTagModel", back_populates="tag")
    tag_similar_text = relationship("TagSimilarTextModel", back_populates="tag")
    board_tag = relationship("BoardTagModel", back_populates="tag")

class TagSimilarTextModel(Base):
    __tablename__ = "tag_similar_text"
    pk = Column(Integer, primary_key=True, index=True)
    tag_pk = Column(Integer, ForeignKey("tag.pk"), nullable=False)
    text = Column(String, index=True, nullable=False)
    version = Column(String, index=True, nullable=False)

    tag = relationship("TagModel", foreign_keys=[tag_pk], back_populates="tag_similar_text")