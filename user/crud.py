from typing import Type

from sqlalchemy.orm import Session

from user.models import *
from user.schemas import *


def getUser(db: Session, user_pk: int) -> UserModel:
    return db.query(UserModel).filter(UserModel.pk == user_pk).first()

def getUserList(db: Session, skip: int = 0, limit: int = 100) -> list[Type[UserModel]]:
    return db.query(UserModel).offset(skip).limit(limit).all()

def createUser(db: Session, user: UserSchema) -> UserModel:
    db_user = UserModel(
        username=user.username,
        password=user.password,
        version=user.version,
        account_expired=user.account_expired,
        account_locked=user.account_locked,
        create_ip=user.create_ip,
        date_created=user.date_created,
        date_withdraw=user.date_withdraw,
        enabled=user.enabled,
        last_password_changed=user.last_password_changed,
        last_update_ip=user.last_update_ip,
        last_updated=user.last_updated,
        password_expired=user.password_expired,
        withdraw=user.withdraw,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def updateUser(db: Session, user_pk: int, update_user: UserSchema) -> UserModel:
    user = getUser(db=db, user_pk=user_pk)
    user.username = update_user.username
    user.password = update_user.password
    db.commit()
    db.refresh(user)
    return user

def deleteUser(db: Session, user_pk: int) -> UserModel:
    user = getUser(db=db, user_pk=user_pk)
    db.delete(user)
    db.commit()
    return user

def getLoggedIn(db: Session, owner_pk: int) -> list[Type[LoggedInModel]]:
    return db.query(LoggedInModel).filter(LoggedInModel.owner_pk == owner_pk)

def createLoggedIn(db: Session, logged_in: LoggedInSchema) -> LoggedInModel:
    db_logged_in = LoggedInModel(
        owner_pk=logged_in.owner_pk,
        version=logged_in.version,
        remote_addr=logged_in.remote_addr,
    )
    db.add(db_logged_in)
    db.commit()
    db.refresh(db_logged_in)
    return db_logged_in

def deleteLoggedIn(db: Session, owner_pk: int) -> LoggedInModel:
    logged_in = getLoggedIn(db=db, owner_pk=owner_pk)
    db.delete(logged_in)
    db.commit()
    return logged_in

def updateLoggedIn(db: Session, owner_pk: int, update_logged_in: LoggedInSchema) -> LoggedInModel:
    logged_in = getLoggedIn(db=db, owner_pk=owner_pk)
    logged_in.version = update_logged_in.version
    logged_in.remote_addr = update_logged_in.remote_addr
    db.commit()
    db.refresh(logged_in)
    return logged_in

def getOauth(db: Session, owner_pk: int) -> list[Type[OauthModel]]:
    return db.query(OauthModel).filter(OauthModel.owner_pk == owner_pk)

def createOauth(db: Session, oauth: OauthSchema) -> OauthModel:
    db_oauth = OauthModel(
        owner_pk=oauth.owner_pk,
        version=oauth.version,
        access_token=oauth.access_token,
        provider=oauth.provider,
    )
    db.add(db_oauth)
    db.commit()
    db.refresh(db_oauth)
    return db_oauth

def deleteOauth(db: Session, owner_pk: int) -> OauthModel:
    oauth = getOauth(db=db, owner_pk=owner_pk)
    db.delete(oauth)
    db.commit()
    return oauth

def updateOauth(db: Session, owner_pk: int, update_oauth: OauthSchema) -> OauthModel:
    oauth = getOauth(db=db, owner_pk=owner_pk)
    oauth.version = update_oauth.version
    oauth.access_token = update_oauth.access_token
    oauth.provider = update_oauth.provider
    db.commit()
    db.refresh(oauth)
    return oauth

def getManagedUser(db: Session, owner_pk: int) -> list[Type[ManagedUserModel]]:
    return db.query(ManagedUserModel).filter(ManagedUserModel.owner_pk == owner_pk)

def createManagedUser(db: Session, managed_user: ManagedUserSchema) -> ManagedUserModel:
    db_managed_user = ManagedUserModel(
        owner_pk=managed_user.owner_pk,
        version=managed_user.version,
    )
    db.add(db_managed_user)
    db.commit()
    db.refresh(db_managed_user)
    return db_managed_user

def updateManagedUser(db: Session, owner_pk: int, update_managed_user: ManagedUserSchema) -> ManagedUserModel:
    managed_user = getManagedUser(db=db, owner_pk=owner_pk)
    managed_user.version = update_managed_user.version
    db.commit()
    db.refresh(managed_user)
    return managed_user

def deleteManagedUser(db: Session, owner_pk: int) -> ManagedUserModel:
    managed_user = getManagedUser(db=db, owner_pk=owner_pk)
    db.delete(managed_user)
    db.commit()
    return managed_user

def getUserRole(db: Session, owner_pk: int) -> list[Type[UserRoleModel]]:
    return db.query(UserRoleModel).filter(UserRoleModel.owner_pk == owner_pk)

def createUserRole(db: Session, user_role: UserRoleSchema) -> UserRoleModel:
    db_role = UserRoleModel(
        owner_pk=user_role.owner_pk,
        role_pk=user_role.role_pk,
    )
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

def updateUserRole(db: Session, owner_pk: int, update_user_role: UserRoleSchema) -> UserRoleModel:
    role = getUserRole(db=db, owner_pk=owner_pk)
    role.role_pk = update_user_role.role_pk
    db.commit()
    db.refresh(role)
    return role

def deleteUserRole(db: Session, owner_pk: int) -> UserRoleModel:
    role = getUserRole(db=db, owner_pk=owner_pk)
    db.delete(role)
    db.commit()
    return role

def getRole(db: Session, role_pk: int) -> list[Type[RoleModel]]:
    return db.query(RoleModel).filter(RoleModel.role_pk == role_pk)

def createRole(db: Session, role: RoleSchema) -> RoleModel:
    db_role = RoleModel(
        version=role.version,
        authority=role.authority,
    )
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

def updateRole(db: Session, role_pk: int, update_role: RoleSchema) -> RoleModel:
    role = getRole(db=db, role_pk=role_pk)
    role.version = update_role.version
    role.name = update_role.name
    db.commit()
    db.refresh(role)
    return role

def deleteRole(db: Session, role_pk: int) -> RoleModel:
    role = getRole(db=db, role_pk=role_pk)
    db.delete(role)
    db.commit()
    return role

def getConfirmEmail(db: Session, owner_pk: int) -> list[Type[ConfirmEmailModel]]:
    return db.query(ConfirmEmailModel).filter(ConfirmEmailModel.owner_pk == owner_pk)

def createConfirmEmail(db: Session, confirm_email: ConfirmEmailSchema) -> ConfirmEmailModel:
    db_confirm_email = ConfirmEmailModel(
        owner_pk=confirm_email.owner_pk,
        version=confirm_email.version,
        date_expired=confirm_email.date_expired,
        email=confirm_email.email,
        secured_key=confirm_email.secured_key
    )
    db.add(db_confirm_email)
    db.commit()
    db.refresh(db_confirm_email)
    return db_confirm_email

def updateConfirmEmail(db: Session, owner_pk: int, update_confirm_email: ConfirmEmailSchema) -> ConfirmEmailModel:
    confirm_email = getConfirmEmail(db=db, owner_pk=owner_pk)
    confirm_email.version = update_confirm_email.version
    confirm_email.date_expired = update_confirm_email.date_expired
    confirm_email.email = update_confirm_email.email
    confirm_email.secured_key = update_confirm_email.secured_key
    db.commit()
    db.refresh(confirm_email)
    return confirm_email

def deleteConfirmEmail(db: Session, owner_pk: int) -> ConfirmEmailModel:
    confirm_email = getConfirmEmail(db=db, owner_pk=owner_pk)
    db.delete(confirm_email)
    db.commit()
    return confirm_email