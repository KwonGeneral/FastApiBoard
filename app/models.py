from typing import Any

from pydantic import BaseModel


class ResponseData(BaseModel):
    # 리턴 데이터 객체
    code: str
    message: str
    data: Any
