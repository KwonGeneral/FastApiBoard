from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import base_result
from app.database import get_db
from app.models import ResponseData
from area import crud
from area.schemas import *

area_router = APIRouter(
    prefix="/area",
    tags=["area"],
    responses={404: {"description": "Not found"}},
)

@area_router.get("/", response_model=ResponseData, description="전체 도시 코드 조회", summary="전체 도시 코드 조회")
async def readAreaCityCodeList(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    areas = crud.getAreaCityCodeList(db, skip=skip, limit=limit)
    return base_result.success(areas)

@area_router.get("/{area_city_code_pk}", response_model=ResponseData, description="특정 도시 코드 조회", summary="특정 도시 코드 조회")
async def readAreaCityCode(area_city_code_pk: int, db: Session = Depends(get_db)):
    db_area = crud.getAreaCityCode(db, area_city_code_pk=area_city_code_pk)
    if db_area is None:
        return base_result.not_found()
    return base_result.success(db_area)

@area_router.post("/", response_model=ResponseData, description="도시 코드 생성", summary="도시 코드 생성")
async def createAreaCityCode(area_city_code: AreaCityCodeSchema, db: Session = Depends(get_db)):
    db_area = crud.getAreaCityCodeByName(db, name=area_city_code.name)
    if db_area:
        return base_result.duplicate()
    return base_result.success(crud.createAreaCityCode(db=db, area_city_code=area_city_code))

@area_router.put("/{area_city_code_pk}", response_model=ResponseData, description="도시 코드 수정", summary="도시 코드 수정")
async def updateAreaCityCode(area_city_code_pk: int, update_area_city_code: AreaCityCodeSchema, db: Session = Depends(get_db)):
    db_area = crud.getAreaCityCode(db, area_city_code_pk=area_city_code_pk)
    if db_area is None:
        return base_result.not_found()
    return base_result.success(crud.updateAreaCityCode(db=db, area_city_code_pk=area_city_code_pk, update_area_city_code=update_area_city_code))

@area_router.delete("/{area_city_code_pk}", response_model=ResponseData, description="도시 코드 삭제", summary="도시 코드 삭제")
async def deleteAreaCityCode(area_city_code_pk: int, db: Session = Depends(get_db)):
    db_area = crud.getAreaCityCode(db, area_city_code_pk=area_city_code_pk)
    if db_area is None:
        return base_result.not_found()
    return base_result.success(crud.deleteAreaCityCode(db=db, area_city_code_pk=area_city_code_pk))

@area_router.get("/district/", response_model=ResponseData, description="전체 구군 코드 조회", summary="전체 구군 코드 조회")
async def readAreaDistrictCodeList(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    areas = crud.getAreaDistrictCodeList(db, skip=skip, limit=limit)
    return base_result.success(areas)

@area_router.get("/district/{area_district_code_pk}", response_model=ResponseData, description="특정 구군 코드 조회", summary="특정 구군 코드 조회")
async def readAreaDistrictCode(area_district_code_pk: int, db: Session = Depends(get_db)):
    db_area = crud.getAreaDistrictCode(db, area_district_code_pk=area_district_code_pk)
    if db_area is None:
        return base_result.not_found()
    return base_result.success(db_area)

@area_router.post("/district/", response_model=ResponseData, description="구군 코드 생성", summary="구군 코드 생성")
async def createAreaDistrictCode(area_district_code: AreaDistrictCodeSchema, db: Session = Depends(get_db)):
    db_area = crud.getAreaDistrictCodeByName(db, name=area_district_code.name)
    if db_area:
        return base_result.duplicate()
    return base_result.success(crud.createAreaDistrictCode(db=db, area_district_code=area_district_code))

@area_router.put("/district/{area_district_code_pk}", response_model=ResponseData, description="구군 코드 수정", summary="구군 코드 수정")
async def updateAreaDistrictCode(area_district_code_pk: int, update_area_district_code: AreaDistrictCodeSchema, db: Session = Depends(get_db)):
    db_area = crud.getAreaDistrictCode(db, area_district_code_pk=area_district_code_pk)
    if db_area is None:
        return base_result.not_found()
    return base_result.success(crud.updateAreaDistrictCode(db=db, area_district_code_pk=area_district_code_pk, update_area_district_code=update_area_district_code))

@area_router.delete("/district/{area_district_code_pk}", response_model=ResponseData, description="구군 코드 삭제", summary="구군 코드 삭제")
async def deleteAreaDistrictCode(area_district_code_pk: int, db: Session = Depends(get_db)):
    db_area = crud.getAreaDistrictCode(db, area_district_code_pk=area_district_code_pk)
    if db_area is None:
        return base_result.not_found()
    return base_result.success(crud.deleteAreaDistrictCode(db=db, area_district_code_pk=area_district_code_pk))