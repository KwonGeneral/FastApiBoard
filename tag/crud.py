from typing import Type

from sqlalchemy.orm import Session

from tag.models import *
from tag.schemas import *

def getTag(db: Session, tag_pk: int) -> TagModel:
    return db.query(TagModel).filter(TagModel.pk == tag_pk).first()

def getTagList(db: Session, skip: int = 0, limit: int = 100) -> list[Type[TagModel]]:
    return db.query(TagModel).offset(skip).limit(limit).all()

def createTag(db: Session, tag: TagSchema) -> TagModel:
    db_tag = TagModel(
        name=tag.name,
        description=tag.description
    )
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag

def updateTag(db: Session, tag_pk: int, update_tag: TagSchema) -> TagModel:
    tag = getTag(db=db, tag_pk=tag_pk)
    tag.name = update_tag.name
    tag.description = update_tag.description
    db.commit()
    db.refresh(tag)
    return tag

def deleteTag(db: Session, tag_pk: int) -> TagModel:
    tag = getTag(db=db, tag_pk=tag_pk)
    db.delete(tag)
    db.commit()
    return tag

def getTagSimilarText(db: Session, tag_similar_text_pk: int) -> TagSimilarTextModel:
    return db.query(TagSimilarTextModel).filter(TagSimilarTextModel.pk == tag_similar_text_pk).first()

def getTagSimilarTextList(db: Session, skip: int = 0, limit: int = 100) -> list[Type[TagSimilarTextModel]]:
    return db.query(TagSimilarTextModel).offset(skip).limit(limit).all()

def createTagSimilarText(db: Session, tag_similar_text: TagSimilarTextSchema) -> TagSimilarTextModel:
    db_tag_similar_text = TagSimilarTextModel(
        tag_pk=tag_similar_text.tag_pk,
        text=tag_similar_text.text,
        version=tag_similar_text.version
    )
    db.add(db_tag_similar_text)
    db.commit()
    db.refresh(db_tag_similar_text)
    return db_tag_similar_text

def updateTagSimilarText(db: Session, tag_similar_text_pk: int, update_tag_similar_text: TagSimilarTextSchema) -> TagSimilarTextModel:
    tag_similar_text = getTagSimilarText(db=db, tag_similar_text_pk=tag_similar_text_pk)
    tag_similar_text.tag_pk = update_tag_similar_text.tag_pk
    tag_similar_text.text = update_tag_similar_text.text
    tag_similar_text.version = update_tag_similar_text.version
    db.commit()
    db.refresh(tag_similar_text)
    return tag_similar_text

def deleteTagSimilarText(db: Session, tag_similar_text_pk: int) -> TagSimilarTextModel:
    tag_similar_text = getTagSimilarText(db=db, tag_similar_text_pk=tag_similar_text_pk)
    db.delete(tag_similar_text)
    db.commit()
    return tag_similar_text