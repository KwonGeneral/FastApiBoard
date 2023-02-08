from datetime import datetime
from typing import Union, Optional
from pydantic import BaseModel
from sqlalchemy import DateTime

from avatar.schemas import AvatarSchema


class UserSchema(BaseModel):
    # 유저 데이터
    version: str  # 버전
    account_expired: Optional[bool] = False  # 계정 만료 여부
    account_locked: Optional[bool] = False  # 계정 잠김 여부
    create_ip: Optional[str] = None  # 생성 IP
    date_created: Optional[datetime] = None  # 생성 일자
    date_withdraw: Optional[datetime] = None  # 탈퇴 일자
    enabled: Optional[bool] = True  # 계정 활성화 여부
    last_password_changed: Optional[datetime] = None  # 마지막 비밀번호 변경 일자
    last_update_ip: Optional[str] = None  # 마지막 수정 IP
    last_updated: Optional[datetime] = None  # 마지막 수정 일자
    password: str  # 비밀번호
    password_expired: Optional[bool] = False  # 비밀번호 만료 여부
    username: str  # 유저 아이디
    withdraw: Optional[bool] = False  # 탈퇴 여부

    class Config:
        orm_mode = True

class UserCreateSchema(BaseModel):
    # 유저 생성 시, 필요한 데이터
    version: str  # 버전
    password: str  # 비밀번호
    username: str  # 유저 아이디
    create_ip: Optional[str] = None  # 생성 IP

class UserUpdateSchema(BaseModel):
    # 유저 수정 시, 필요한 데이터
    version: Optional[str] = None  # 버전
    password: Optional[str] = None  # 비밀번호
    create_ip: Optional[str] = None  # 생성 IP


class LoggedInSchema(BaseModel):
    # 로그인 데이터
    owner_pk: int  # 유저 고유 번호
    version: str  # 버전
    remote_addr: Optional[str] = None  # 접속 IP

    class Config:
        orm_mode = True

class OauthSchema(BaseModel):
    # 인증 데이터
    owner_pk: int  # 유저 고유 번호
    version: str  # 버전
    access_token: str  # 액세스 토큰
    provider: str  # 인증 제공자

    class Config:
        orm_mode = True

class ManagedUserSchema(BaseModel):
    # 유저 관리 데이터
    owner_pk: int  # 유저 고유 번호
    version: str  # 버전

    class Config:
        orm_mode = True

class UserRoleSchema(BaseModel):
    # 유저 권한 데이터
    owner_pk: int  # 유저 고유 번호
    role_pk: int  # 권한 고유 번호

    class Config:
        orm_mode = True

class RoleSchema(BaseModel):
    # 권한 데이터
    version: str  # 버전
    authority: str  # 권한

    class Config:
        orm_mode = True

class ConfirmEmailSchema(BaseModel):
    # 이메일 확인 데이터
    owner_pk: int  # 유저 고유 번호
    version: str  # 버전
    email: str  # 이메일
    secured_key: str  # 확인 코드
    date_expired: datetime  # 만료 일자

    class Config:
        orm_mode = True