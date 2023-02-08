from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import base_result
from app.database import get_db
from app.models import ResponseData
from banner import crud
from banner.schemas import *

banner_router = APIRouter(
    prefix="/banner",
    tags=["banner"],
    responses={404: {"description": "Not found"}},
)

@banner_router.get("/", response_model=ResponseData, description="전체 배너 조회", summary="전체 배너 조회")
async def readBannerList(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    banners = crud.getBannerList(db, skip=skip, limit=limit)
    return base_result.success(banners)

@banner_router.get("/{banner_pk}", response_model=ResponseData, description="특정 배너 조회", summary="특정 배너 조회")
async def readBanner(banner_pk: int, db: Session = Depends(get_db)):
    db_banner = crud.getBanner(db, banner_pk=banner_pk)
    if db_banner is None:
        return base_result.not_found()
    return base_result.success(db_banner)

@banner_router.post("/", response_model=ResponseData, description="배너 생성", summary="배너 생성")
async def createBanner(banner: BannerSchema, db: Session = Depends(get_db)):
    db_banner = crud.createBanner(db, banner)
    return base_result.success(db_banner)

@banner_router.put("/{banner_pk}", response_model=ResponseData, description="배너 수정", summary="배너 수정")
async def updateBanner(banner_pk: int, banner: BannerSchema, db: Session = Depends(get_db)):
    db_banner = crud.updateBanner(db, banner_pk, banner)
    if db_banner is None:
        return base_result.not_found()
    return base_result.success(db_banner)

@banner_router.delete("/{banner_pk}", response_model=ResponseData, description="배너 삭제", summary="배너 삭제")
async def deleteBanner(banner_pk: int, db: Session = Depends(get_db)):
    db_banner = crud.deleteBanner(db, banner_pk)
    if db_banner is None:
        return base_result.not_found()
    return base_result.success(db_banner)

@banner_router.get("/click/", response_model=ResponseData, description="배너 클릭수 전체 조회", summary="배너 클릭수 전체 조회")
async def readBannerClickList(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    banner_clicks = crud.getBannerClickList(db, skip=skip, limit=limit)
    return base_result.success(banner_clicks)

@banner_router.get("/click/{banner_click_pk}", response_model=ResponseData, description="배너 클릭수 조회", summary="배너 클릭수 조회")
async def readBannerClick(banner_click_pk: int, db: Session = Depends(get_db)):
    banner_click = crud.getBannerClick(db, banner_click_pk=banner_click_pk)
    if banner_click is None:
        return base_result.not_found()
    return base_result.success(banner_click)

@banner_router.post("/click/", response_model=ResponseData, description="배너 클릭수 생성", summary="배너 클릭수 생성")
async def createBannerClick(banner_click: BannerClickSchema, db: Session = Depends(get_db)):
    db_banner_click = crud.createBannerClick(db, banner_click)
    return base_result.success(db_banner_click)

@banner_router.put("/click/{banner_click_pk}", response_model=ResponseData, description="배너 클릭수 수정", summary="배너 클릭수 수정")
async def updateBannerClick(banner_click_pk: int, banner_click: BannerClickSchema, db: Session = Depends(get_db)):
    db_banner_click = crud.updateBannerClick(db, banner_click_pk, banner_click)
    if db_banner_click is None:
        return base_result.not_found()
    return base_result.success(db_banner_click)

@banner_router.delete("/click/{banner_click_pk}", response_model=ResponseData, description="배너 클릭수 삭제", summary="배너 클릭수 삭제")
async def deleteBannerClick(banner_click_pk: int, db: Session = Depends(get_db)):
    db_banner_click = crud.deleteBannerClick(db, banner_click_pk)
    if db_banner_click is None:
        return base_result.not_found()
    return base_result.success(db_banner_click)
