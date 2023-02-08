from typing import Any

from fastapi import HTTPException
from pydantic import BaseModel

from app.models import ResponseData

ERROR_CODE = "400"
SUCCESS_CODE = "200"

def not_found() -> ResponseData:
    return ResponseData(
        code=ERROR_CODE,
        message="해당하는 데이터를 찾지 못했습니다.",
        data=None
    )

def exception() -> ResponseData:
    return ResponseData(
        code=ERROR_CODE,
        message="올바른 접근이 아닙니다.",
        data=None
    )

def duplicate() -> ResponseData:
    return ResponseData(
        code=ERROR_CODE,
        message="이미 존재하는 데이터입니다.",
        data=None
    )

def success(data: Any) -> ResponseData:
    return ResponseData(
        code=SUCCESS_CODE,
        message="정상적으로 처리되었습니다.",
        data=data
    )