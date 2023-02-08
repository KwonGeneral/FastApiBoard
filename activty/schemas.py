from datetime import datetime
from typing import Union, Optional
from pydantic import BaseModel
from sqlalchemy import DateTime

class ActivitySchema(BaseModel):
    # 활동 데이터
    avatar_pk: int
    board_pk: int
    content_pk: int
    version: str
    point: int
    point_type: str
    type: str

    class Config:
        orm_mode = True