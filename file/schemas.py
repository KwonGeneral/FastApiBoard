from datetime import datetime
from typing import Union, Optional
from pydantic import BaseModel
from sqlalchemy import DateTime


class FileSchema(BaseModel):
    # 파일 데이터
    version:str  # 파일 버전
    attach_type: str  # 파일 종류
    byte_size: int  # 파일 크기
    height: int  # 파일 높이
    name: str  # 파일 이름
    org_name: str  # 파일 원본 이름
    type: str  # 파일 타입
    width: int  # 파일 너비

    class Config:
        orm_mode = True