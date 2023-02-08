from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import base_result
from app.database import get_db
from app.models import ResponseData
from tag import crud
from tag.schemas import *

tag_router = APIRouter(
    prefix="/tag",
    tags=["tag"],
    responses={404: {"description": "Not found"}},
)

@tag_router.get("/", response_model=ResponseData, description="전체 태그 조회", summary="전체 태그 조회")
async def readTagList(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tags = crud.getTagList(db, skip=skip, limit=limit)
    return base_result.success(tags)

@tag_router.get("/{tag_pk}", response_model=ResponseData, description="특정 태그 조회", summary="특정 태그 조회")
async def readTag(tag_pk: int, db: Session = Depends(get_db)):
    db_tag = crud.getTag(db, tag_pk=tag_pk)
    if db_tag is None:
        return base_result.not_found()
    return base_result.success(db_tag)

@tag_router.post("/", response_model=ResponseData, description="태그 생성", summary="태그 생성")
async def createTag(tag: TagSchema, db: Session = Depends(get_db)):
    db_tag = crud.createTag(db, tag)
    return base_result.success(db_tag)

@tag_router.put("/{tag_pk}", response_model=ResponseData, description="태그 수정", summary="태그 수정")
async def updateTag(tag_pk: int, update_tag: TagSchema, db: Session = Depends(get_db)):
    db_tag = crud.updateTag(db, tag_pk=tag_pk, update_tag=update_tag)
    return base_result.success(db_tag)

@tag_router.delete("/{tag_pk}", response_model=ResponseData, description="태그 삭제", summary="태그 삭제")
async def deleteTag(tag_pk: int, db: Session = Depends(get_db)):
    db_tag = crud.deleteTag(db, tag_pk=tag_pk)
    return base_result.success(db_tag)

@tag_router.get("/similar/", response_model=ResponseData, description="유사 태그 조회", summary="유사 태그 조회")
async def readSimilarTagList(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tags = crud.getTagSimilarTextList(db, skip=skip, limit=limit)
    return base_result.success(tags)

@tag_router.get("/similar/{tag_similar_text_pk}", response_model=ResponseData, description="특정 태그의 유사 태그 조회", summary="특정 태그의 유사 태그 조회")
async def readSimilarTag(tag_similar_text_pk: int, db: Session = Depends(get_db)):
    db_tag = crud.getTagSimilarText(db, tag_similar_text_pk=tag_similar_text_pk)
    if db_tag is None:
        return base_result.not_found()
    return base_result.success(db_tag)

@tag_router.post("/similar/", response_model=ResponseData, description="유사 태그 생성", summary="유사 태그 생성")
async def createSimilarTag(tag: TagSimilarTextSchema, db: Session = Depends(get_db)):
    db_tag = crud.createTagSimilarText(db, tag)
    return base_result.success(db_tag)

@tag_router.put("/similar/{tag_similar_text_pk}", response_model=ResponseData, description="유사 태그 수정", summary="유사 태그 수정")
async def updateSimilarTag(tag_similar_text_pk: int, update_tag_similar_text: TagSimilarTextSchema, db: Session = Depends(get_db)):
    db_tag = crud.updateTagSimilarText(db, tag_similar_text_pk=tag_similar_text_pk, update_tag_similar_text=update_tag_similar_text)
    return base_result.success(db_tag)

@tag_router.delete("/similar/{tag_similar_text_pk}", response_model=ResponseData, description="유사 태그 삭제", summary="유사 태그 삭제")
async def deleteSimilarTag(tag_similar_text_pk: int, db: Session = Depends(get_db)):
    db_tag = crud.deleteTagSimilarText(db, tag_similar_text_pk=tag_similar_text_pk)
    return base_result.success(db_tag)