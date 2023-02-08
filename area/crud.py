from typing import Type

from sqlalchemy.orm import Session

from area.models import *
from area.schemas import *

def getAreaCityCode(db: Session, area_city_code_pk: int) -> AreaCityCodeModel:
    return db.query(AreaCityCodeModel).filter(AreaCityCodeModel.pk == area_city_code_pk).first()

def getAreaCityCodeList(db: Session, skip: int = 0, limit: int = 100) -> list[Type[AreaCityCodeModel]]:
    return db.query(AreaCityCodeModel).offset(skip).limit(limit).all()

def getAreaCityCodeByName(db: Session, name: str) -> AreaCityCodeModel:
    return db.query(AreaCityCodeModel).filter(AreaCityCodeModel.name == name).first()

def createAreaCityCode(db: Session, area_city_code: AreaCityCodeSchema) -> AreaCityCodeModel:
    db_area_city_code = AreaCityCodeModel(
        version=area_city_code.version,
        name=area_city_code.name,
    )
    db.add(db_area_city_code)
    db.commit()
    db.refresh(db_area_city_code)
    return db_area_city_code

def updateAreaCityCode(db: Session, area_city_code_pk: int, update_area_city_code: AreaCityCodeSchema) -> AreaCityCodeModel:
    area_city_code = getAreaCityCode(db=db, area_city_code_pk=area_city_code_pk)
    area_city_code.name = update_area_city_code.name
    area_city_code.version = update_area_city_code.version
    db.commit()
    db.refresh(area_city_code)
    return area_city_code

def deleteAreaCityCode(db: Session, area_city_code_pk: int) -> AreaCityCodeModel:
    area_city_code = getAreaCityCode(db=db, area_city_code_pk=area_city_code_pk)
    db.delete(area_city_code)
    db.commit()
    return area_city_code

def getAreaDistrictCode(db: Session, area_district_code_pk: int) -> AreaDistrictCodeModel:
    return db.query(AreaDistrictCodeModel).filter(AreaDistrictCodeModel.pk == area_district_code_pk).first()

def getAreaDistrictCodeList(db: Session, skip: int = 0, limit: int = 100) -> list[Type[AreaDistrictCodeModel]]:
    return db.query(AreaDistrictCodeModel).offset(skip).limit(limit).all()

def getAreaDistrictCodeByName(db: Session, name: str) -> AreaDistrictCodeModel:
    return db.query(AreaDistrictCodeModel).filter(AreaDistrictCodeModel.name == name).first()

def createAreaDistrictCode(db: Session, area_district_code: AreaDistrictCodeSchema) -> AreaDistrictCodeModel:
    db_area_district_code = AreaDistrictCodeModel(
        version=area_district_code.version,
        name=area_district_code.name,
        area_city_code_pk=area_district_code.area_city_code_pk,
    )
    db.add(db_area_district_code)
    db.commit()
    db.refresh(db_area_district_code)
    return db_area_district_code

def updateAreaDistrictCode(db: Session, area_district_code_pk: int, update_area_district_code: AreaDistrictCodeSchema) -> AreaDistrictCodeModel:
    area_district_code = getAreaDistrictCode(db=db, area_district_code_pk=area_district_code_pk)
    area_district_code.name = update_area_district_code.name
    area_district_code.version = update_area_district_code.version
    area_district_code.area_city_code_pk = update_area_district_code.area_city_code_pk
    db.commit()
    db.refresh(area_district_code)
    return area_district_code

def deleteAreaDistrictCode(db: Session, area_district_code_pk: int) -> AreaDistrictCodeModel:
    area_district_code = getAreaDistrictCode(db=db, area_district_code_pk=area_district_code_pk)
    db.delete(area_district_code)
    db.commit()
    return area_district_code