from datetime import datetime
from typing import Union, Optional
from pydantic import BaseModel
from sqlalchemy import DateTime

class BannerSchema(BaseModel):
    # 배너 데이터
    version: str  # 배너 버전
    date_created: Optional[datetime] = None  # 생성 일자
    last_updated: Optional[datetime] = None  # 수정 일자
    image: Optional[str]  # 배너 이미지
    name: str  # 배너 이름
    target: Optional[str]  # 배너 타겟
    type: str  # 배너 타입
    url: str  # 배너 URL
    visible: bool  # 배너 표시 여부

    class Config:
        orm_mode = True

class BannerClickSchema(BaseModel):
    # 배너 클릭 데이터
    version: str  # 배너 버전
    banner_pk: int  # 배너 고유 번호
    date_created: Optional[datetime] = None  # 생성 일자
    ip: str  # 클릭 IP

    class Config:
        orm_mode = True