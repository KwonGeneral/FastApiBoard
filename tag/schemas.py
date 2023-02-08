from datetime import datetime
from typing import Union, Optional
from pydantic import BaseModel
from sqlalchemy import DateTime


class TagSchema(BaseModel):
    # 태그 데이터
    date_created: Optional[datetime] = None  # 생성 일자
    name: str  # 태그 이름
    description: Optional[str] = None  # 태그 설명

    class Config:
        orm_mode = True


class TagSimilarTextSchema(BaseModel):
    tag_pk: int
    text: str
    version: str

    class Config:
        orm_mode = True