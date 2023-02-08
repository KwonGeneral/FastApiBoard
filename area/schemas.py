from datetime import datetime
from typing import Union, Optional
from pydantic import BaseModel
from sqlalchemy import DateTime

class AreaCityCodeSchema(BaseModel):
    # 도시 코드 데이터
    version: str
    name: str

    class Config:
        orm_mode = True

class AreaDistrictCodeSchema(BaseModel):
    # 구, 군 코드 데이터
    version: str
    name: str
    area_city_code_pk: int

    class Config:
        orm_mode = True