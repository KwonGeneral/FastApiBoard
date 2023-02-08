from datetime import datetime
from typing import Union, Optional
from pydantic import BaseModel
from sqlalchemy import DateTime

class AvatarSchema(BaseModel):
    # 아바타 데이터
    owner_pk: int  # 소유자 고유 번호
    version: str  # 아바타 버전
    activity_point: int  # 활동 포인트
    nick_name: str  # 닉네임
    official: Optional[bool]  # 공식 아바타 여부
    picture: str  # 프로필 사진
    picture_type: int # 프로필 사진 타입

    class Config:
        orm_mode = True

class AvatarTagSchema(BaseModel):
    # 아바타 태그 데이터
    avatar_pk: int  # 아바타 고유 번호
    tag_pk: int  # 태그 고유 번호

    class Config:
        orm_mode = True

class NotificationSchema(BaseModel):
    # 알림 데이터
    sender_pk: int  # 발신자 고유 번호
    receiver_pk: int  # 수신자 고유 번호
    version: str  # 알림 버전
    date_created: Optional[datetime] = None  # 생성 일자
    last_updated: Optional[datetime] = None  # 수정 일자
    type: str  # 알림 타입

    class Config:
        orm_mode = True