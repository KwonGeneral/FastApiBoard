import datetime
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

class BoardModel(Base):
    __tablename__ = "board"
    pk = Column(Integer, primary_key=True, index=True)
    category_pk = Column(Integer, ForeignKey("category.pk"), nullable=False)
    owner_pk = Column(Integer, ForeignKey("avatar.pk"), nullable=True)
    content_pk = Column(Integer, ForeignKey("content.pk"), nullable=True)
    last_editor_pk = Column(Integer, ForeignKey("avatar.pk"), nullable=True)
    version = Column(String, index=True, nullable=False)
    a_nick_name = Column(String, index=True, nullable=True)
    anonymity = Column(Boolean, default=False, nullable=False)
    choice = Column(Boolean, default=False, nullable=False)
    create_ip = Column(String, index=True, nullable=True)
    date_created = Column(DateTime, default=datetime.datetime.utcnow, index=True, nullable=False)
    enabled = Column(Boolean, default=True, nullable=False)
    is_recruit = Column(Boolean, default=False, nullable=False)
    last_updated = Column(DateTime, default=datetime.datetime.utcnow, index=True, nullable=False)
    scrap_count = Column(Integer, default=0, nullable=False)
    tag_string = Column(String, index=True, nullable=True)
    title = Column(String, index=True, nullable=False)
    board_count = Column(Integer, default=0, nullable=False)
    view_count = Column(Integer, default=0, nullable=False)
    vote_count = Column(Integer, default=0, nullable=False)

    category = relationship("CategoryModel", foreign_keys="CategoryModel.board_pk", back_populates="board")
    content = relationship("ContentModel", foreign_keys="ContentModel.board_pk", back_populates="board")
    owner = relationship("AvatarModel", foreign_keys=[owner_pk], back_populates="board_owner")
    last_editor = relationship("AvatarModel", foreign_keys=[last_editor_pk], back_populates="board_last_editor")
    activity = relationship("ActivityModel", back_populates="board")
    content_vote = relationship("ContentVoteModel", back_populates="board")
    scrap = relationship("ScrapModel", back_populates="board")
    change_log = relationship("ChangeLogModel", back_populates="board")
    board_tag = relationship("BoardTagModel", back_populates="board")

class ContentModel(Base):
    __tablename__ = "content"
    pk = Column(Integer, primary_key=True, index=True)
    board_pk = Column(Integer, ForeignKey("board.pk"), nullable=True)
    owner_pk = Column(Integer, ForeignKey("avatar.pk"), nullable=True)
    version = Column(String, index=True, nullable=False)
    a_nick_name = Column(String, index=True, nullable=True)
    anonymity = Column(Boolean, default=False, nullable=False)
    create_ip = Column(String, index=True, nullable=True)
    date_created = Column(DateTime, default=datetime.datetime.utcnow, index=True, nullable=False)
    last_editor_pk = Column(Integer, ForeignKey("avatar.pk"), nullable=True)
    last_updated = Column(DateTime, default=datetime.datetime.utcnow, index=True, nullable=False)
    selected = Column(Boolean, default=False, nullable=False)
    text = Column(String, index=True, nullable=False)
    text_type = Column(Integer, index=True, nullable=False)
    type = Column(Integer, index=True, nullable=False)
    vote_count = Column(Integer, default=0, index=True, nullable=False)

    board = relationship("BoardModel", foreign_keys=[board_pk], back_populates="content")
    owner = relationship("AvatarModel", foreign_keys=[owner_pk], back_populates="content_owner")
    last_editor = relationship("AvatarModel", foreign_keys=[last_editor_pk], back_populates="content_last_editor")
    activity = relationship("ActivityModel", back_populates="content")
    content_vote = relationship("ContentVoteModel", foreign_keys="ContentVoteModel.content_pk", back_populates="content")
    content_file = relationship("ContentFileModel", foreign_keys="ContentFileModel.content_pk", back_populates="content")
    change_log = relationship("ChangeLogModel", back_populates="content")
    opinion = relationship("OpinionModel", back_populates="content")

class ContentVoteModel(Base):
    __tablename__ = "content_vote"
    pk = Column(Integer, primary_key=True, index=True)
    content_pk = Column(Integer, ForeignKey("content.pk"), nullable=False)
    owner_pk = Column(Integer, ForeignKey("avatar.pk"), nullable=False)
    board_pk = Column(Integer, ForeignKey("board.pk"), nullable=False)
    date_created = Column(DateTime, default=datetime.datetime.utcnow, index=True, nullable=False)
    point = Column(Integer, index=True, nullable=False)

    content = relationship("ContentModel", foreign_keys=[content_pk], back_populates="content_vote")
    owner = relationship("AvatarModel", foreign_keys=[owner_pk], back_populates="content_vote")
    board = relationship("BoardModel", foreign_keys=[board_pk], back_populates="content_vote")

class ContentFileModel(Base):
    __tablename__ = "content_file"
    pk = Column(Integer, primary_key=True, index=True)
    content_pk = Column(Integer, ForeignKey("content.pk"), nullable=False)
    file_pk = Column(Integer, ForeignKey("file.pk"), nullable=False)

    content = relationship("ContentModel", foreign_keys=[content_pk], back_populates="content_file")
    file = relationship("FileModel", foreign_keys=[file_pk], back_populates="content_file")

class ChangeLogModel(Base):
    __tablename__ = "change_log"
    pk = Column(Integer, primary_key=True, index=True)
    version = Column(String, index=True, nullable=False)
    board_pk = Column(Integer, ForeignKey("board.pk"), nullable=False)
    avatar_pk = Column(Integer, ForeignKey("avatar.pk"), nullable=True)
    content_pk = Column(Integer, ForeignKey("content.pk"), nullable=True)
    date_created = Column(DateTime, default=datetime.datetime.utcnow, index=True, nullable=False)
    md5 = Column(String, index=True, nullable=False)
    patch = Column(String, index=True, nullable=False)
    revision = Column(Integer, index=True, nullable=False)
    type = Column(String, index=True, nullable=False)

    board = relationship("BoardModel", foreign_keys=[board_pk], back_populates="change_log")
    avatar = relationship("AvatarModel", foreign_keys=[avatar_pk], back_populates="change_log")
    content = relationship("ContentModel", foreign_keys=[content_pk], back_populates="change_log")

class BoardTagModel(Base):
    __tablename__ = "board_tag"
    pk = Column(Integer, primary_key=True, index=True)
    board_pk = Column(Integer, ForeignKey("board.pk"), nullable=False)
    tag_pk = Column(Integer, ForeignKey("tag.pk"), nullable=False)

    board = relationship("BoardModel", foreign_keys=[board_pk], back_populates="board_tag")
    tag = relationship("TagModel", foreign_keys=[tag_pk], back_populates="board_tag")

class CategoryModel(Base):
    __tablename__ = "category"
    pk = Column(Integer, primary_key=True, index=True)
    board_pk = Column(Integer, ForeignKey("board.pk"), nullable=True)
    version = Column(String, index=True, nullable=False)
    anonymity = Column(Boolean, default=False, nullable=True)
    date_created = Column(DateTime, default=datetime.datetime.utcnow, index=True, nullable=False)
    default_label = Column(String, index=True, nullable=False)
    enabled = Column(Boolean, default=False, nullable=False)
    external_link = Column(String, index=True, nullable=True)
    icon_css_names = Column(String, index=True, nullable=True)
    isurl = Column(Boolean, default=False, nullable=False)
    label_code = Column(String, index=True, nullable=False)
    last_updated = Column(DateTime, default=datetime.datetime.utcnow, index=True, nullable=False)
    level = Column(Integer, index=True, nullable=False)
    require_tag = Column(Boolean, default=False, nullable=False)
    sort_order = Column(Integer, index=True, nullable=False)
    url = Column(String, index=True, nullable=True)
    use_evaluate = Column(Boolean, default=False, nullable=False)
    use_note = Column(Boolean, default=False, nullable=False)
    use_opinion = Column(Boolean, default=False, nullable=False)
    use_tag = Column(Boolean, default=False, nullable=False)
    writable = Column(Boolean, default=False, nullable=False)
    write_by_external_link = Column(Boolean, default=False, nullable=True)

    board = relationship("BoardModel", foreign_keys=[board_pk], back_populates="category")

class OpinionModel(Base):
    __tablename__ = "opinion"
    pk = Column(Integer, primary_key=True, index=True)
    content_pk = Column(Integer, ForeignKey("content.pk"), nullable=False)
    owner_pk = Column(Integer, ForeignKey("avatar.pk"), nullable=False)
    version = Column(String, index=True, nullable=False)
    comment = Column(String, index=True, nullable=True)
    date_created = Column(DateTime, default=datetime.datetime.utcnow, index=True, nullable=False)
    last_updated = Column(DateTime, default=datetime.datetime.utcnow, index=True, nullable=False)
    vote_count = Column(Integer, default=0, index=True, nullable=False)

    content = relationship("ContentModel", foreign_keys=[content_pk], back_populates="opinion")
    owner = relationship("AvatarModel", foreign_keys=[owner_pk], back_populates="opinion")


class SpamWordModel(Base):
    __tablename__ = "spam_word"
    pk = Column(Integer, primary_key=True, index=True)
    version = Column(String, index=True, nullable=False)
    text = Column(String, index=True, nullable=False)


class ScrapModel(Base):
    __tablename__ = "scrap"
    pk = Column(Integer, primary_key=True, index=True)
    owner_pk = Column(Integer, ForeignKey("avatar.pk"), nullable=False)
    board_pk = Column(Integer, ForeignKey("board.pk"), nullable=False)
    version = Column(String, index=True, nullable=False)
    date_created = Column(DateTime, default=datetime.datetime.utcnow, index=True, nullable=False)

    board = relationship("BoardModel", foreign_keys=[board_pk], back_populates="scrap")
    owner = relationship("AvatarModel", foreign_keys=[owner_pk], back_populates="scrap")