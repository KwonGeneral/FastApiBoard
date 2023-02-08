from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import base_result
from app.database import get_db
from app.models import ResponseData
from file import crud
from file.schemas import *

file_router = APIRouter(
    prefix="/file",
    tags=["file"],
    responses={404: {"description": "Not found"}},
)

@file_router.get("/", response_model=ResponseData, description="전체 파일 조회", summary="전체 파일 조회")
async def readFileList(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    file_list = crud.getFileList(db, skip=skip, limit=limit)
    return base_result.success(file_list)

@file_router.get("/{file_pk}", response_model=ResponseData, description="특정 파일 조회", summary="특정 파일 조회")
async def readFile(file_pk: int, db: Session = Depends(get_db)):
    db_file = crud.getFile(db, file_pk=file_pk)
    if db_file is None:
        return base_result.not_found()
    return base_result.success(db_file)

@file_router.post("/", response_model=ResponseData, description="파일 생성", summary="파일 생성")
async def createFile(file: FileSchema, db: Session = Depends(get_db)):
    return base_result.success(crud.createFile(db, file))

@file_router.put("/{file_pk}", response_model=ResponseData, description="파일 수정", summary="파일 수정")
async def updateFile(file_pk: int, update_file: FileSchema, db: Session = Depends(get_db)):
    db_file = crud.getFile(db, file_pk=file_pk)
    if db_file is None:
        return base_result.not_found()
    return base_result.success(crud.updateFile(db, file_pk, update_file))

@file_router.delete("/{file_pk}", response_model=ResponseData, description="파일 삭제", summary="파일 삭제")
async def deleteFile(file_pk: int, db: Session = Depends(get_db)):
    db_file = crud.getFile(db, file_pk=file_pk)
    if db_file is None:
        return base_result.not_found()
    return base_result.success(crud.deleteFile(db, file_pk))