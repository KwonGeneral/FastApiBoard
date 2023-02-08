import datetime

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from app.database import Base


class UserModel(Base):
    __tablename__ = "user"
    pk = Column(Integer, primary_key=True, index=True)
    avatar_pk = Column(Integer, ForeignKey("avatar.pk"), nullable=False)
    version = Column(String, index=True, nullable=False)
    account_expired = Column(Boolean, default=False, index=True, nullable=False)
    account_locked = Column(Boolean, default=False, index=True, nullable=False)
    create_ip = Column(String, index=True, nullable=True)
    date_created = Column(DateTime, default=datetime.datetime.utcnow, index=True, nullable=False)
    date_withdraw = Column(DateTime, index=True, nullable=True)
    enabled = Column(Boolean, default=True, index=True, nullable=False)
    last_password_changed = Column(DateTime, default=datetime.datetime.utcnow, index=True, nullable=False)
    last_update_ip = Column(String, index=True, nullable=True)
    last_updated = Column(DateTime, default=datetime.datetime.utcnow, index=True, nullable=False)
    password = Column(String, index=True, nullable=False)
    password_expired = Column(Boolean, default=False, index=True, nullable=False)
    username = Column(String, index=True, nullable=False)
    withdraw = Column(Boolean, default=False, index=True, nullable=False)
    
    avatar = relationship("AvatarModel", foreign_keys="AvatarModel.owner_pk", back_populates="owner")
    logged_in = relationship("LoggedInModel", back_populates="owner")
    oauth = relationship("OauthModel", back_populates="owner")
    managed_user = relationship("ManagedUserModel", back_populates="owner")
    user_role = relationship("UserRoleModel", back_populates="owner")
    confirm_email = relationship("ConfirmEmailModel", back_populates="owner")

class LoggedInModel(Base):
    __tablename__ = "logged_in"
    pk = Column(Integer, primary_key=True, index=True)
    owner_pk = Column(Integer, ForeignKey("user.pk"), nullable=False)
    version = Column(String, index=True, nullable=False)
    date_created = Column(DateTime, default=datetime.datetime.utcnow, index=True, nullable=False)
    remote_addr = Column(String, index=True, nullable=True)

    owner = relationship("UserModel", foreign_keys=[owner_pk], back_populates="logged_in")
    
class OauthModel(Base):
    __tablename__ = "oauth"
    pk = Column(Integer, primary_key=True, index=True)
    owner_pk = Column(Integer, ForeignKey("user.pk"), nullable=False)
    version = Column(String, index=True, nullable=False)
    access_token = Column(String, index=True, nullable=False)
    provider = Column(String, index=True, nullable=False)

    owner = relationship("UserModel", foreign_keys=[owner_pk], back_populates="oauth")
    
class ManagedUserModel(Base):
    __tablename__ = "managed_user"
    pk = Column(Integer, primary_key=True, index=True)
    owner_pk = Column(Integer, ForeignKey("user.pk"), nullable=False)
    version = Column(String, index=True, nullable=False)

    owner = relationship("UserModel", foreign_keys=[owner_pk], back_populates="managed_user")

class UserRoleModel(Base):
    __tablename__ = "user_role"
    pk = Column(Integer, primary_key=True, index=True)
    owner_pk = Column(Integer, ForeignKey("user.pk"), nullable=False)
    role_pk = Column(Integer, ForeignKey("role.pk"), nullable=False)

    owner = relationship("UserModel", foreign_keys=[owner_pk], back_populates="user_role")
    role = relationship("RoleModel", foreign_keys=[role_pk], back_populates="user_role")

class RoleModel(Base):
    __tablename__ = "role"
    pk = Column(Integer, primary_key=True, index=True)
    version = Column(String, index=True, nullable=False)
    authority = Column(String, index=True, nullable=False)

    user_role = relationship("UserRoleModel", back_populates="role")

class ConfirmEmailModel(Base):
    __tablename__ = "confirm_email"
    pk = Column(Integer, primary_key=True, index=True)
    owner_pk = Column(Integer, ForeignKey("user.pk"), nullable=False)
    version = Column(String, index=True, nullable=False)
    date_expired = Column(DateTime, default=datetime.datetime.utcnow, index=True, nullable=False)
    email = Column(String, index=True, nullable=False)
    secured_key = Column(String, index=True, nullable=False)

    owner = relationship("UserModel", foreign_keys=[owner_pk], back_populates="confirm_email")