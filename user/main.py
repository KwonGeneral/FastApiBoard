from typing import Type, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import base_result
from app.database import get_db
from app.models import ResponseData
from user import crud
from user.schemas import *

user_router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)

@user_router.get("/", response_model=ResponseData, description="전체 유저 조회", summary="전체 유저 조회")
async def readUserList(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    user_list = crud.getUserList(db=db, skip=skip, limit=limit)
    return base_result.success(user_list)

@user_router.get("/{user_pk}", response_model=ResponseData, description="특정 유저 조회", summary="특정 유저 조회")
async def readUser(user_pk: int, db: Session = Depends(get_db)):
    user = crud.getUser(db=db, user_pk=user_pk)
    if user is None:
        return base_result.not_found()
    return base_result.success(user)

@user_router.post("/", response_model=ResponseData, description="유저 생성", summary="유저 생성")
async def createUser(user: UserSchema, db: Session = Depends(get_db)):
    return base_result.success(crud.createUser(db=db, user=user))

@user_router.put("/{user_pk}", response_model=ResponseData, description="유저 수정", summary="유저 수정")
async def updateUser(user_pk: int, update_user: UserSchema, db: Session = Depends(get_db)):
    user = crud.getUser(db=db, user_pk=user_pk)
    if user is None:
        return base_result.not_found()
    return base_result.success(crud.updateUser(db=db, user_pk=user_pk, update_user=update_user))

@user_router.delete("/{user_pk}", response_model=ResponseData, description="유저 삭제", summary="유저 삭제")
async def deleteUser(user_pk: int, db: Session = Depends(get_db)):
    user = crud.getUser(db=db, user_pk=user_pk)
    if user is None:
        return base_result.not_found()
    return base_result.success(crud.deleteUser(db=db, user_pk=user_pk))

@user_router.get("/loggedin/", response_model=ResponseData, description="특정 유저 로그인 기록 조회", summary="특정 유저 로그인 기록 조회")
async def readLoggedIn(owner_pk: int, db: Session = Depends(get_db)):
    user = crud.getLoggedInList(db=db, owner_pk=owner_pk)
    if user is None:
        return base_result.not_found()
    return base_result.success(user)

@user_router.post("/loggedin/", response_model=ResponseData, description="유저 로그인 기록 생성", summary="유저 로그인 기록 생성")
async def createLoggedIn(logged_in: LoggedInSchema, db: Session = Depends(get_db)):
    return base_result.success(crud.createLoggedIn(db=db, logged_in=logged_in))

@user_router.put("/loggedin/{owner_pk}", response_model=ResponseData, description="유저 로그인 기록 수정", summary="유저 로그인 기록 수정")
async def updateLoggedIn(owner_pk: int, update_logged_in: LoggedInSchema, db: Session = Depends(get_db)):
    logged_in = crud.getLoggedIn(db=db, owner_pk=owner_pk)
    if logged_in is None:
        return base_result.not_found()
    return base_result.success(crud.updateLoggedIn(db=db, owner_pk=owner_pk, update_logged_in=update_logged_in))

@user_router.delete("/loggedin/{logged_in_pk}", response_model=ResponseData, description="유저 로그인 기록 삭제", summary="유저 로그인 기록 삭제")
async def deleteLoggedIn(logged_in_pk: int, db: Session = Depends(get_db)):
    logged_in = crud.getLoggedIn(db=db, owner_pk=logged_in_pk)
    if logged_in is None:
        return base_result.not_found()
    return base_result.success(crud.deleteLoggedIn(db=db, owner_pk=logged_in_pk))

@user_router.get("/oauth/", response_model=ResponseData, description="특정 유저 Oauth 조회", summary="특정 유저 Oauth 조회")
async def readOauth(owner_pk: int, db: Session = Depends(get_db)):
    user = crud.getOauthList(db=db, owner_pk=owner_pk)
    if user is None:
        return base_result.not_found()
    return base_result.success(user)

@user_router.post("/oauth/", response_model=ResponseData, description="유저 Oauth 생성", summary="유저 Oauth 생성")
async def createOauth(oauth: OauthSchema, db: Session = Depends(get_db)):
    return base_result.success(crud.createOauth(db=db, oauth=oauth))

@user_router.put("/oauth/{owner_pk}", response_model=ResponseData, description="유저 Oauth 수정", summary="유저 Oauth 수정")
async def updateOauth(owner_pk: int, update_oauth: OauthSchema, db: Session = Depends(get_db)):
    oauth = crud.getOauth(db=db, owner_pk=owner_pk)
    if oauth is None:
        return base_result.not_found()
    return base_result.success(crud.updateOauth(db=db, owner_pk=owner_pk, update_oauth=update_oauth))

@user_router.delete("/oauth/{oauth_pk}", response_model=ResponseData, description="유저 Oauth 삭제", summary="유저 Oauth 삭제")
async def deleteOauth(oauth_pk: int, db: Session = Depends(get_db)):
    oauth = crud.getOauth(db=db, owner_pk=oauth_pk)
    if oauth is None:
        return base_result.not_found()
    return base_result.success(crud.deleteOauth(db=db, owner_pk=oauth_pk))

@user_router.get("/managed/", response_model=ResponseData, description="특정 유저 관리자 조회", summary="특정 유저 관리자 조회")
async def readManagedUser(owner_pk: int, db: Session = Depends(get_db)):
    user = crud.getManagedUserList(db=db, owner_pk=owner_pk)
    if user is None:
        return base_result.not_found()
    return base_result.success(user)

@user_router.post("/managed/", response_model=ResponseData, description="유저 관리자 생성", summary="유저 관리자 생성")
async def createManagedUser(managed_user: ManagedUserSchema, db: Session = Depends(get_db)):
    return base_result.success(crud.createManagedUser(db=db, managed_user=managed_user))

@user_router.put("/managed/{owner_pk}", response_model=ResponseData, description="유저 관리자 수정", summary="유저 관리자 수정")
async def updateManagedUser(owner_pk: int, update_managed_user: ManagedUserSchema, db: Session = Depends(get_db)):
    managed_user = crud.getManagedUser(db=db, owner_pk=owner_pk)
    if managed_user is None:
        return base_result.not_found()
    return base_result.success(crud.updateManagedUser(db=db, owner_pk=owner_pk, update_managed_user=update_managed_user))

@user_router.delete("/managed/{managed_user_pk}", response_model=ResponseData, description="유저 관리자 삭제", summary="유저 관리자 삭제")
async def deleteManagedUser(managed_user_pk: int, db: Session = Depends(get_db)):
    managed_user = crud.getManagedUser(db=db, owner_pk=managed_user_pk)
    if managed_user is None:
        return base_result.not_found()
    return base_result.success(crud.deleteManagedUser(db=db, owner_pk=managed_user_pk))

@user_router.get("/userrole/", response_model=ResponseData, description="특정 유저 권한 조회", summary="특정 유저 권한 조회")
async def readUserRole(owner_pk: int, db: Session = Depends(get_db)):
    user = crud.getUserRole(db=db, owner_pk=owner_pk)
    if user is None:
        return base_result.not_found()
    return base_result.success(user)

@user_router.post("/userrole/", response_model=ResponseData, description="유저 권한 생성", summary="유저 권한 생성")
async def createUserRole(user_role: UserRoleSchema, db: Session = Depends(get_db)):
    return base_result.success(crud.createUserRole(db=db, user_role=user_role))

@user_router.put("/userrole/{owner_pk}", response_model=ResponseData, description="유저 권한 수정", summary="유저 권한 수정")
async def updateUserRole(owner_pk: int, update_user_role: UserRoleSchema, db: Session = Depends(get_db)):
    user_role = crud.getUserRole(db=db, owner_pk=owner_pk)
    if user_role is None:
        return base_result.not_found()
    return base_result.success(crud.updateUserRole(db=db, owner_pk=owner_pk, update_user_role=update_user_role))

@user_router.delete("/userrole/{user_role_pk}", response_model=ResponseData, description="유저 권한 삭제", summary="유저 권한 삭제")
async def deleteUserRole(user_role_pk: int, db: Session = Depends(get_db)):
    user_role = crud.getUserRole(db=db, owner_pk=user_role_pk)
    if user_role is None:
        return base_result.not_found()
    return base_result.success(crud.deleteUserRole(db=db, owner_pk=user_role_pk))

@user_router.get("/role/", response_model=ResponseData, description="특정 권한 조회", summary="특정 권한 조회")
async def readRole(role_pk: int, db: Session = Depends(get_db)):
    user = crud.getRole(db=db, role_pk=role_pk)
    if user is None:
        return base_result.not_found()
    return base_result.success(user)

@user_router.post("/role/", response_model=ResponseData, description="권한 생성", summary="권한 생성")
async def createRole(role: RoleSchema, db: Session = Depends(get_db)):
    return base_result.success(crud.createRole(db=db, role=role))

@user_router.put("/role/{role_pk}", response_model=ResponseData, description="권한 수정", summary="권한 수정")
async def updateRole(role_pk: int, update_role: RoleSchema, db: Session = Depends(get_db)):
    role = crud.getRole(db=db, role_pk=role_pk)
    if role is None:
        return base_result.not_found()
    return base_result.success(crud.updateRole(db=db, role_pk=role_pk, update_role=update_role))

@user_router.delete("/role/{role_pk}", response_model=ResponseData, description="권한 삭제", summary="권한 삭제")
async def deleteRole(role_pk: int, db: Session = Depends(get_db)):
    role = crud.getRole(db=db, role_pk=role_pk)
    if role is None:
        return base_result.not_found()
    return base_result.success(crud.deleteRole(db=db, role_pk=role_pk))

@user_router.get("/confirm/", response_model=ResponseData, description="이메일 인증", summary="이메일 인증")
async def getConfirmEmail(owner_pk: int, db: Session = Depends(get_db)):
    user = crud.getConfirmEmail(db=db, owner_pk=owner_pk)
    if user is None:
        return base_result.not_found()
    return base_result.success(user)

@user_router.post("/confirm/", response_model=ResponseData, description="이메일 인증 생성", summary="이메일 인증 생성")
async def createConfirmEmail(confirm_email: ConfirmEmailSchema, db: Session = Depends(get_db)):
    return base_result.success(crud.createConfirmEmail(db=db, confirm_email=confirm_email))

@user_router.put("/confirm/{confirm_email_pk}", response_model=ResponseData, description="이메일 인증 수정", summary="이메일 인증 수정")
async def updateConfirmEmail(confirm_email_pk: int, update_confirm_email: ConfirmEmailSchema, db: Session = Depends(get_db)):
    confirm_email = crud.getConfirmEmail(db=db, owner_pk=confirm_email_pk)
    if confirm_email is None:
        return base_result.not_found()
    return base_result.success(crud.updateConfirmEmail(db=db, owner_pk=confirm_email_pk, update_confirm_email=update_confirm_email))

@user_router.delete("/confirm/{confirm_email_pk}", response_model=ResponseData, description="이메일 인증 삭제", summary="이메일 인증 삭제")
async def deleteConfirmEmail(confirm_email_pk: int, db: Session = Depends(get_db)):
    confirm_email = crud.getConfirmEmail(db=db, owner_pk=confirm_email_pk)
    if confirm_email is None:
        return base_result.not_found()
    return base_result.success(crud.deleteConfirmEmail(db=db, owner_pk=confirm_email_pk))