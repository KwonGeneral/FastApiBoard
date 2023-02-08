from typing import Type

from sqlalchemy.orm import Session

from board.models import *
from board.schemas import *

def getBoard(db: Session, board_pk: int) -> BoardModel:
    return db.query(BoardModel).filter(BoardModel.pk == board_pk).first()

def getBoardList(db: Session, skip: int = 0, limit: int = 100) -> list[Type[BoardModel]]:
    return db.query(BoardModel).offset(skip).limit(limit).all()

def createBoard(db: Session, board: BoardSchema) -> BoardModel:
    db_board = BoardModel(
        category_pk=board.category_pk,
        owner_pk=board.owner_pk,
        content_pk=board.content_pk,
        last_editor_pk=board.last_editor_pk,
        version=board.version,
        a_nick_name=board.a_nick_name,
        anonymity=board.anonymity,
        choice=board.choice,
        create_ip=board.create_ip,
        enabled=board.enabled,
        is_recruit=board.is_recruit,
        tag_string=board.tag_string,
        title=board.title,
    )
    db.add(db_board)
    db.commit()
    db.refresh(db_board)
    return db_board

def deleteBoard(db: Session, board_pk: int) -> BoardModel:
    board = getBoard(db=db, board_pk=board_pk)
    db.delete(board)
    db.commit()
    return board

def updateBoard(db: Session, board_pk: int, update_board: BoardSchema) -> BoardModel:
    board = getBoard(db=db, board_pk=board_pk)
    board.category_pk = update_board.category_pk
    board.owner_pk = update_board.owner_pk
    board.content_pk = update_board.content_pk
    board.last_editor_pk = update_board.last_editor_pk
    board.version = update_board.version
    board.a_nick_name = update_board.a_nick_name
    board.anonymity = update_board.anonymity
    board.choice = update_board.choice
    board.create_ip = update_board.create_ip
    board.enabled = update_board.enabled
    board.is_recruit = update_board.is_recruit
    board.tag_string = update_board.tag_string
    board.title = update_board.title
    db.commit()
    db.refresh(board)
    return board

def getContentVote(db: Session, content_vote_pk: int) -> ContentVoteModel:
    return db.query(ContentVoteModel).filter(ContentVoteModel.pk == content_vote_pk).first()

def getContentVoteList(db: Session, skip: int = 0, limit: int = 100) -> list[Type[ContentVoteModel]]:
    return db.query(ContentVoteModel).offset(skip).limit(limit).all()

def createContentVote(db: Session, content_vote: ContentVoteSchema) -> ContentVoteModel:
    db_content_vote = ContentVoteModel(
        content_pk=content_vote.content_pk,
        file_pk=content_vote.file_pk,
    )
    db.add(db_content_vote)
    db.commit()
    db.refresh(db_content_vote)
    return db_content_vote

def deleteContentVote(db: Session, content_vote_pk: int) -> ContentVoteModel:
    content_vote = getContentVote(db=db, content_vote_pk=content_vote_pk)
    db.delete(content_vote)
    db.commit()
    return content_vote

def updateContentVote(db: Session, content_vote_pk: int, update_content_vote: ContentVoteSchema) -> ContentVoteModel:
    content_vote = getContentVote(db=db, content_vote_pk=content_vote_pk)
    content_vote.content_pk = update_content_vote.content_pk
    content_vote.file_pk = update_content_vote.file_pk
    db.commit()
    db.refresh(content_vote)
    return content_vote

def getChangeLog(db: Session, change_log_pk: int) -> ChangeLogModel:
    return db.query(ChangeLogModel).filter(ChangeLogModel.pk == change_log_pk).first()

def getChangeLogList(db: Session, skip: int = 0, limit: int = 100) -> list[Type[ChangeLogModel]]:
    return db.query(ChangeLogModel).offset(skip).limit(limit).all()

def createChangeLog(db: Session, change_log: ChangeLogSchema) -> ChangeLogModel:
    db_change_log = ChangeLogModel(
        version=change_log.version,
        board_pk=change_log.board_pk,
        avatar_pk=change_log.avatar_pk,
        content_pk=change_log.content_pk,
        md5=change_log.md5,
        patch=change_log.patch,
        revision=change_log.revision,
        type=change_log.type,
    )
    db.add(db_change_log)
    db.commit()
    db.refresh(db_change_log)
    return db_change_log

def deleteChangeLog(db: Session, change_log_pk: int) -> ChangeLogModel:
    change_log = getChangeLog(db=db, change_log_pk=change_log_pk)
    db.delete(change_log)
    db.commit()
    return change_log

def updateChangeLog(db: Session, change_log_pk: int, update_change_log: ChangeLogSchema) -> ChangeLogModel:
    change_log = getChangeLog(db=db, change_log_pk=change_log_pk)
    change_log.version = update_change_log.version
    change_log.board_pk = update_change_log.board_pk
    change_log.avatar_pk = update_change_log.avatar_pk
    change_log.content_pk = update_change_log.content_pk
    change_log.md5 = update_change_log.md5
    change_log.patch = update_change_log.patch
    change_log.revision = update_change_log.revision
    change_log.type = update_change_log.type
    db.commit()
    db.refresh(change_log)
    return change_log

def getBoardTag(db: Session, board_tag_pk: int) -> BoardTagModel:
    return db.query(BoardTagModel).filter(BoardTagModel.pk == board_tag_pk).first()

def getBoardTagList(db: Session, skip: int = 0, limit: int = 100) -> list[Type[BoardTagModel]]:
    return db.query(BoardTagModel).offset(skip).limit(limit).all()

def createBoardTag(db: Session, board_tag: BoardTagSchema) -> BoardTagModel:
    db_board_tag = BoardTagModel(
        board_pk=board_tag.board_pk,
        tag_pk=board_tag.tag_pk,
    )
    db.add(db_board_tag)
    db.commit()
    db.refresh(db_board_tag)
    return db_board_tag

def deleteBoardTag(db: Session, board_tag_pk: int) -> BoardTagModel:
    board_tag = getBoardTag(db=db, board_tag_pk=board_tag_pk)
    db.delete(board_tag)
    db.commit()
    return board_tag

def updateBoardTag(db: Session, board_tag_pk: int, update_board_tag: BoardTagSchema) -> BoardTagModel:
    board_tag = getBoardTag(db=db, board_tag_pk=board_tag_pk)
    board_tag.board_pk = update_board_tag.board_pk
    board_tag.tag_pk = update_board_tag.tag_pk
    db.commit()
    db.refresh(board_tag)
    return board_tag

def getCategory(db: Session, category_pk: int) -> CategoryModel:
    return db.query(CategoryModel).filter(CategoryModel.pk == category_pk).first()

def getCategoryList(db: Session, skip: int = 0, limit: int = 100) -> list[Type[CategoryModel]]:
    return db.query(CategoryModel).offset(skip).limit(limit).all()

def createCategory(db: Session, category: CategorySchema) -> CategoryModel:
    db_category = CategoryModel(
        board_pk=category.board_pk,
        version=category.version,
        anonymity=category.anonymity,
        default_label=category.default_label,
        enabled=category.enabled,
        external_link=category.external_link,
        icon_css_names=category.icon_css_names,
        isurl=category.isurl,
        label_code=category.label_code,
        level=category.level,
        require_tag=category.require_tag,
        sort_order=category.sort_order,
        url=category.url,
        use_evaluate=category.use_evaluate,
        use_note=category.use_note,
        use_opinion=category.use_opinion,
        use_tag=category.use_tag,
        writable=category.writable,
        write_by_external_link=category.write_by_external_link,
    )
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def deleteCategory(db: Session, category_pk: int) -> CategoryModel:
    category = getCategory(db=db, category_pk=category_pk)
    db.delete(category)
    db.commit()
    return category

def updateCategory(db: Session, category_pk: int, update_category: CategorySchema) -> CategoryModel:
    category = getCategory(db=db, category_pk=category_pk)
    category.board_pk = update_category.board_pk
    category.version = update_category.version
    category.anonymity = update_category.anonymity
    category.default_label = update_category.default_label
    category.enabled = update_category.enabled
    category.external_link = update_category.external_link
    category.icon_css_names = update_category.icon_css_names
    category.isurl = update_category.isurl
    category.label_code = update_category.label_code
    category.level = update_category.level
    category.require_tag = update_category.require_tag
    category.sort_order = update_category.sort_order
    category.url = update_category.url
    category.use_evaluate = update_category.use_evaluate
    category.use_note = update_category.use_note
    category.use_opinion = update_category.use_opinion
    category.use_tag = update_category.use_tag
    category.writable = update_category.writable
    category.write_by_external_link = update_category.write_by_external_link
    db.commit()
    db.refresh(category)
    return category

def getOpinion(db: Session, opinion_pk: int) -> OpinionModel:
    return db.query(OpinionModel).filter(OpinionModel.pk == opinion_pk).first()

def getOpinionList(db: Session, skip: int = 0, limit: int = 100) -> list[Type[OpinionModel]]:
    return db.query(OpinionModel).offset(skip).limit(limit).all()

def createOpinion(db: Session, opinion: OpinionSchema) -> OpinionModel:
    db_opinion = OpinionModel(
        content_pk=opinion.content_pk,
        owner_pk=opinion.owner_pk,
        version=opinion.version,
        comment=opinion.comment,
    )
    db.add(db_opinion)
    db.commit()
    db.refresh(db_opinion)
    return db_opinion

def deleteOpinion(db: Session, opinion_pk: int) -> OpinionModel:
    opinion = getOpinion(db=db, opinion_pk=opinion_pk)
    db.delete(opinion)
    db.commit()
    return opinion

def updateOpinion(db: Session, opinion_pk: int, update_opinion: OpinionSchema) -> OpinionModel:
    opinion = getOpinion(db=db, opinion_pk=opinion_pk)
    opinion.content_pk = update_opinion.content_pk
    opinion.owner_pk = update_opinion.owner_pk
    opinion.version = update_opinion.version
    opinion.comment = update_opinion.comment
    db.commit()
    db.refresh(opinion)
    return opinion

def getSpamWord(db: Session, spam_word_pk: int) -> SpamWordModel:
    return db.query(SpamWordModel).filter(SpamWordModel.pk == spam_word_pk).first()

def getSpamWordList(db: Session, skip: int = 0, limit: int = 100) -> list[Type[SpamWordModel]]:
    return db.query(SpamWordModel).offset(skip).limit(limit).all()

def createSpamWord(db: Session, spam_word: SpamWordSchema) -> SpamWordModel:
    db_spam_word = SpamWordModel(
        version=spam_word.version,
        text=spam_word.text,
    )
    db.add(db_spam_word)
    db.commit()
    db.refresh(db_spam_word)
    return db_spam_word

def deleteSpamWord(db: Session, spam_word_pk: int) -> SpamWordModel:
    spam_word = getSpamWord(db=db, spam_word_pk=spam_word_pk)
    db.delete(spam_word)
    db.commit()
    return spam_word

def updateSpamWord(db: Session, spam_word_pk: int, update_spam_word: SpamWordSchema) -> SpamWordModel:
    spam_word = getSpamWord(db=db, spam_word_pk=spam_word_pk)
    spam_word.version = update_spam_word.version
    spam_word.text = update_spam_word.text
    db.commit()
    db.refresh(spam_word)
    return spam_word