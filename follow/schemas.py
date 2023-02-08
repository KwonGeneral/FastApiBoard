from datetime import datetime
from typing import Union, Optional
from pydantic import BaseModel
from sqlalchemy import DateTime


class FollowSchema(BaseModel):
    # 팔로우 데이터
    date_created: Optional[datetime] = None  # 생성 일자
    follower_pk: int  # 팔로워 고유 번호
    following_pk: int  # 팔로잉 고유 번호

    class Config:
        orm_mode = True