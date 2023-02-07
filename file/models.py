import datetime
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

class FileModel(Base):
    __tablename__ = "file"
    pk = Column(Integer, primary_key=True, index=True)
    version = Column(String, index=True, nullable=False)
    attach_type = Column(String, index=True, nullable=False)
    byte_size = Column(Integer, index=True, nullable=False)
    height = Column(Integer, index=True, nullable=False)
    name = Column(String, index=True, nullable=False)
    org_name = Column(String, index=True, nullable=False)
    type = Column(String, index=True, nullable=False)
    width = Column(Integer, index=True, nullable=False)