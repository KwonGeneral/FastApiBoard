import datetime
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

class AreaCityCodeModel(Base):
    __tablename__ = "area_city_code"
    pk = Column(Integer, primary_key=True, index=True)
    version = Column(String, index=True, nullable=False)
    name = Column(String, index=True, nullable=False)

    area_district_code = relationship("AreaDistrictCodeModel", back_populates="area_city_code")

class AreaDistrictCodeModel(Base):
    __tablename__ = "area_district_code"
    pk = Column(Integer, primary_key=True, index=True)
    version = Column(String, index=True, nullable=False)
    name = Column(String, index=True, nullable=False)
    area_city_code_pk = Column(Integer, ForeignKey("area_city_code.pk"), nullable=False)

    area_city_code = relationship("AreaCityCodeModel", foreign_keys=[area_city_code_pk], back_populates="area_district_code")