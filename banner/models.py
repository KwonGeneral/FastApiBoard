import datetime
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

class BannerModel(Base):
    __tablename__ = "banner"
    pk = Column(Integer, primary_key=True, index=True)
    version = Column(String, index=True, nullable=False)
    date_created = Column(DateTime, default=datetime.datetime.utcnow, index=True, nullable=False)
    last_updated = Column(DateTime, default=datetime.datetime.utcnow, index=True, nullable=False)
    image = Column(String, index=True, nullable=True)
    name = Column(String, index=True, nullable=False)
    target = Column(String, index=True, nullable=True)
    type = Column(String, index=True, nullable=False)
    url = Column(String, index=True, nullable=False)
    visible = Column(Boolean, default=True, index=True, nullable=False)

class BannerClickModel(Base):
    __tablename__ = "banner_click"
    pk = Column(Integer, primary_key=True, index=True)
    version = Column(String, index=True, nullable=False)
    banner_pk = Column(Integer, ForeignKey("banner.pk"), nullable=False)
    click_count = Column(Integer, index=True, nullable=False)
    date_created = Column(DateTime, default=datetime.datetime.utcnow, index=True, nullable=False)
    ip = Column(String, index=True, nullable=False)

    banner = relationship("BannerModel", back_populates="banner_click")