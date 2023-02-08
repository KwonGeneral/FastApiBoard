from typing import Type

from sqlalchemy.orm import Session

from file.models import *
from file.schemas import *

def getFile(db: Session, file_pk: int) -> FileModel:
    return db.query(FileModel).filter(FileModel.pk == file_pk).first()

def getFileList(db: Session, skip: int = 0, limit: int = 100) -> list[Type[FileModel]]:
    return db.query(FileModel).offset(skip).limit(limit).all()

def createFile(db: Session, file: FileSchema) -> FileModel:
    db_file = FileModel(
        version=file.version,
        attach_type=file.attach_type,
        byte_size=file.byte_size,
        height=file.height,
        name=file.name,
        org_name=file.org_name,
        type=file.type,
        width=file.width,
    )
    db.add(db_file)
    db.commit()
    db.refresh(db_file)
    return db_file

def deleteFile(db: Session, file_pk: int) -> FileModel:
    file = getFile(db=db, file_pk=file_pk)
    db.delete(file)
    db.commit()
    return file

def updateFile(db: Session, file_pk: int, update_file: FileSchema) -> FileModel:
    file = getFile(db=db, file_pk=file_pk)
    file.version = update_file.version
    file.attach_type = update_file.attach_type
    file.byte_size = update_file.byte_size
    file.height = update_file.height
    file.name = update_file.name
    file.org_name = update_file.org_name
    file.type = update_file.type
    file.width = update_file.width
    db.commit()
    db.refresh(file)
    return file