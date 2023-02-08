from datetime import datetime
from typing import Union, Optional
from pydantic import BaseModel
from sqlalchemy import DateTime

class BoardSchema(BaseModel):
    # 게시글 데이터
    category_pk: int  # 카테고리 고유 번호
    owner_pk: Optional[int] = None  # 게시글 소유자 고유 번호
    content_pk: Optional[int] = None  # 게시글 내용 고유 번호
    last_editor_pk: Optional[int] = None  # 게시글 마지막 수정자 고유 번호
    version: str  # 게시글 버전
    a_nick_name: Optional[str] = None  # 게시글 작성자 닉네임
    anonymity: bool  # 익명 여부
    choice: bool  # 게시글 선택
    create_ip: Optional[str] = None  # 게시글 작성 IP
    date_created: Optional[datetime] = None  # 게시글 작성 일자
    enabled: bool  # 게시글 활성화 여부
    is_recruit: bool  # 모집 여부
    last_updated: Optional[datetime] = None  # 게시글 마지막 수정 일자
    tag_string: Optional[str] = None  # 태그 문자열
    title: str  # 게시글 제목

    class Config:
        orm_mode = True

class ContentSchema(BaseModel):
    # 게시글 내용 데이터
    board_pk: Optional[int] = None  # 게시글 고유 번호
    owner_pk: Optional[int] = None  # 게시글 소유자 고유 번호
    version: str  # 게시글 버전
    a_nick_name: Optional[str] = None  # 게시글 작성자 닉네임
    anonymity: bool  # 익명 여부
    create_ip: Optional[str] = None  # 게시글 작성 IP
    date_created: Optional[datetime] = None  # 게시글 작성 일자
    last_editor_pk: Optional[int] = None  # 게시글 마지막 수정자 고유 번호
    last_updated: Optional[datetime] = None  # 게시글 마지막 수정 일자
    selected: bool  # 게시글 선택
    text: str  # 게시글 내용
    text_type: int  # 게시글 내용 타입
    type: int  # 게시글 타입

    class Config:
        orm_mode = True

class ContentVoteSchema(BaseModel):
    # 게시글 투표 데이터
    content_pk: int  # 게시글 고유 번호
    file_pk: int  # 파일 고유 번호

    class Config:
        orm_mode = True

class ChangeLogSchema(BaseModel):
    # 게시글 변경 로그 데이터
    version: str  # 게시글 버전
    board_pk: int  # 게시글 고유 번호
    avatar_pk: Optional[int]  # 게시글 작성자 아바타 고유 번호
    content_pk: Optional[int]  # 게시글 내용 고유 번호
    date_created: Optional[datetime]  # 게시글 작성 일자
    md5: str  # 게시글 작성자 아바타 MD5
    patch: str  # 게시글 변경 내용
    revision: int  # 게시글 변경 횟수
    type: int  # 게시글 변경 타입

    class Config:
        orm_mode = True

class BoardTagSchema(BaseModel):
    # 게시글 태그 데이터
    board_pk: int  # 게시글 고유 번호
    tag_pk: int  # 태그 고유 번호

    class Config:
        orm_mode = True

class CategorySchema(BaseModel):
    # 카테고리 데이터
    board_pk: Optional[int]  # 게시글 고유 번호
    version: str  # 게시글 버전
    anonymity: Optional[bool]  # 익명 여부
    date_created: Optional[datetime]  # 게시글 작성 일자
    default_label: str  # 기본 라벨
    enabled: bool  # 활성화 여부
    external_link: Optional[str]  # 외부 링크
    icon_css_names: Optional[str]  # 아이콘 CSS 이름
    isurl: bool  # URL 여부
    label_code: str  # 라벨 코드
    last_updated: Optional[datetime]  # 게시글 마지막 수정 일자
    level: int  # 레벨
    require_tag: bool  # 태그 필수 여부
    sort_order: int  # 정렬 순서
    url: Optional[str]  # URL
    use_evaluate: bool  # 평가 사용 여부
    use_note: bool  # 노트 사용 여부
    use_opinion: bool  # 의견 사용 여부
    use_tag: bool  # 태그 사용 여부
    writable: bool  # 작성 가능 여부
    write_by_external_link: bool  # 외부 링크 작성 여부

    class Config:
        orm_mode = True

class OpinionSchema(BaseModel):
    # 의견 데이터
    content_pk: int  # 게시글 고유 번호
    owner_pk: int  # 게시글 작성자 고유 번호
    version: str  # 게시글 버전
    comment: Optional[str]  # 의견 내용
    date_created: Optional[datetime]  # 의견 작성 일자
    last_updated: Optional[datetime]  # 의견 마지막 수정 일자

    class Config:
        orm_mode = True

class SpamWordSchema(BaseModel):
    # 스팸 단어 데이터
    version: str  # 게시글 버전
    text: str  # 스팸 단어

    class Config:
        orm_mode = True