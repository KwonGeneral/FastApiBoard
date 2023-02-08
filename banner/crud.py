from typing import Type

from sqlalchemy.orm import Session

from banner.models import *
from banner.schemas import *

def getBanner(db: Session, banner_pk: int) -> BannerModel:
    return db.query(BannerModel).filter(BannerModel.pk == banner_pk).first()

def getBannerList(db: Session, skip: int = 0, limit: int = 100) -> list[Type[BannerModel]]:
    return db.query(BannerModel).offset(skip).limit(limit).all()

def createBanner(db: Session, banner: BannerSchema) -> BannerModel:
    db_banner = BannerModel(
        version=banner.version,
        image=banner.image,
        name=banner.name,
        target=banner.target,
        type=banner.type,
        url=banner.url,
        visible=banner.visible,
    )
    db.add(db_banner)
    db.commit()
    db.refresh(db_banner)
    return db_banner

def updateBanner(db: Session, banner_pk: int, update_banner: BannerSchema) -> BannerModel:
    banner = getBanner(db=db, banner_pk=banner_pk)
    banner.version = update_banner.version
    banner.image = update_banner.image
    banner.name = update_banner.name
    banner.target = update_banner.target
    banner.type = update_banner.type
    banner.url = update_banner.url
    banner.visible = update_banner.visible
    db.commit()
    db.refresh(banner)
    return banner

def deleteBanner(db: Session, banner_pk: int) -> BannerModel:
    banner = getBanner(db=db, banner_pk=banner_pk)
    db.delete(banner)
    db.commit()
    return banner

def getBannerClick(db: Session, banner_click_pk: int) -> BannerClickModel:
    return db.query(BannerClickModel).filter(BannerClickModel.pk == banner_click_pk).first()

def getBannerClickList(db: Session, skip: int = 0, limit: int = 100) -> list[Type[BannerClickModel]]:
    return db.query(BannerClickModel).offset(skip).limit(limit).all()

def createBannerClick(db: Session, banner_click: BannerClickSchema) -> BannerClickModel:
    db_banner_click = BannerClickModel(
        banner_pk=banner_click.banner_pk,
        ip=banner_click.ip,
        version=banner_click.version,
    )
    db.add(db_banner_click)
    db.commit()
    db.refresh(db_banner_click)
    return db_banner_click

def updateBannerClick(db: Session, banner_click_pk: int, update_banner_click: BannerClickSchema) -> BannerClickModel:
    banner_click = getBannerClick(db=db, banner_click_pk=banner_click_pk)
    banner_click.banner_pk = update_banner_click.banner_pk
    banner_click.ip = update_banner_click.ip
    banner_click.version = update_banner_click.version
    db.commit()
    db.refresh(banner_click)
    return banner_click

def deleteBannerClick(db: Session, banner_click_pk: int) -> BannerClickModel:
    banner_click = getBannerClick(db=db, banner_click_pk=banner_click_pk)
    db.delete(banner_click)
    db.commit()
    return banner_click