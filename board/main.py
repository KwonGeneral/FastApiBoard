from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import base_result
from app.database import get_db
from app.models import ResponseData
from board import crud
from board.schemas import *

board_router = APIRouter(
    prefix="/board",
    tags=["board"],
    responses={404: {"description": "Not found"}},
)

@board_router.get("/", response_model=ResponseData, description="전체 게시글 조회", summary="전체 게시글 조회")
async def readBoardList(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    board_list = crud.getBoardList(db, skip=skip, limit=limit)
    return base_result.success(board_list)

@board_router.get("/{board_pk}", response_model=ResponseData, description="특정 게시글 조회", summary="특정 게시글 조회")
async def readBoard(board_pk: int, db: Session = Depends(get_db)):
    db_board = crud.getBoard(db, board_pk=board_pk)
    if db_board is None:
        return base_result.not_found()
    return base_result.success(db_board)

@board_router.post("/", response_model=ResponseData, description="게시글 생성", summary="게시글 생성")
async def createBoard(board: BoardSchema, db: Session = Depends(get_db)):
    return base_result.success(crud.createBoard(db, board))

@board_router.put("/{board_pk}", response_model=ResponseData, description="게시글 수정", summary="게시글 수정")
async def updateBoard(board_pk: int, update_board: BoardSchema, db: Session = Depends(get_db)):
    db_board = crud.getBoard(db, board_pk=board_pk)
    if db_board is None:
        return base_result.not_found()
    return base_result.success(crud.updateBoard(db, board_pk, update_board))

@board_router.delete("/{board_pk}", response_model=ResponseData, description="게시글 삭제", summary="게시글 삭제")
async def deleteBoard(board_pk: int, db: Session = Depends(get_db)):
    db_board = crud.getBoard(db, board_pk=board_pk)
    if db_board is None:
        return base_result.not_found()
    return base_result.success(crud.deleteBoard(db, board_pk))

@board_router.get("/content/", response_model=ResponseData, description="전체 게시글 내용 조회", summary="전체 게시글 내용 조회")
async def readContentList(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    content_list = crud.getContentList(db, skip=skip, limit=limit)
    return base_result.success(content_list)

@board_router.get("/content/{content_pk}", response_model=ResponseData, description="특정 게시글 내용 조회", summary="특정 게시글 내용 조회")
async def readContent(content_pk: int, db: Session = Depends(get_db)):
    db_content = crud.getContent(db, content_pk=content_pk)
    if db_content is None:
        return base_result.not_found()
    return base_result.success(db_content)

@board_router.post("/content/", response_model=ResponseData, description="게시글 내용 생성", summary="게시글 내용 생성")
async def createContent(content: ContentSchema, db: Session = Depends(get_db)):
    return base_result.success(crud.createContent(db, content))

@board_router.put("/content/{content_pk}", response_model=ResponseData, description="게시글 내용 수정", summary="게시글 내용 수정")
async def updateContent(content_pk: int, update_content: ContentSchema, db: Session = Depends(get_db)):
    db_content = crud.getContent(db, content_pk=content_pk)
    if db_content is None:
        return base_result.not_found()
    return base_result.success(crud.updateContent(db, content_pk, update_content))

@board_router.delete("/content/{content_pk}", response_model=ResponseData, description="게시글 내용 삭제", summary="게시글 내용 삭제")
async def deleteContent(content_pk: int, db: Session = Depends(get_db)):
    db_content = crud.getContent(db, content_pk=content_pk)
    if db_content is None:
        return base_result.not_found()
    return base_result.success(crud.deleteContent(db, content_pk))

@board_router.get("/content/vote/", response_model=ResponseData, description="게시글 추천 조회", summary="게시글 추천 조회")
async def readContentVoteList(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    content_vote_list = crud.getContentVoteList(db, skip=skip, limit=limit)
    return base_result.success(content_vote_list)

@board_router.get("/content/vote/{content_vote_pk}", response_model=ResponseData, description="특정 게시글 추천 조회", summary="특정 게시글 추천 조회")
async def readContentVote(content_vote_pk: int, db: Session = Depends(get_db)):
    db_content_vote = crud.getContentVote(db, content_vote_pk=content_vote_pk)
    if db_content_vote is None:
        return base_result.not_found()
    return base_result.success(db_content_vote)

@board_router.post("/content/vote/", response_model=ResponseData, description="게시글 추천 생성", summary="게시글 추천 생성")
async def createContentVote(content_vote: ContentVoteSchema, db: Session = Depends(get_db)):
    return base_result.success(crud.createContentVote(db, content_vote))

@board_router.put("/content/vote/{content_vote_pk}", response_model=ResponseData, description="게시글 추천 수정", summary="게시글 추천 수정")
async def updateContentVote(content_vote_pk: int, update_content_vote: ContentVoteSchema, db: Session = Depends(get_db)):
    db_content_vote = crud.getContentVote(db, content_vote_pk=content_vote_pk)
    if db_content_vote is None:
        return base_result.not_found()
    return base_result.success(crud.updateContentVote(db, content_vote_pk, update_content_vote))

@board_router.delete("/content/vote/{content_vote_pk}", response_model=ResponseData, description="게시글 추천 삭제", summary="게시글 추천 삭제")
async def deleteContentVote(content_vote_pk: int, db: Session = Depends(get_db)):
    db_content_vote = crud.getContentVote(db, content_vote_pk=content_vote_pk)
    if db_content_vote is None:
        return base_result.not_found()
    return base_result.success(crud.deleteContentVote(db, content_vote_pk))

@board_router.get("/changelog/", response_model=ResponseData, description="게시글 변경 이력 조회", summary="게시글 변경 이력 조회")
async def readChangeLogList(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    changelog_list = crud.getChangeLogList(db, skip=skip, limit=limit)
    return base_result.success(changelog_list)

@board_router.get("/changelog/{change_log_pk}", response_model=ResponseData, description="특정 게시글 변경 이력 조회", summary="특정 게시글 변경 이력 조회")
async def readChangeLog(change_log_pk: int, db: Session = Depends(get_db)):
    db_changelog = crud.getChangeLog(db, change_log_pk=change_log_pk)
    if db_changelog is None:
        return base_result.not_found()
    return base_result.success(db_changelog)

@board_router.post("/changelog/", response_model=ResponseData, description="게시글 변경 이력 생성", summary="게시글 변경 이력 생성")
async def createChangeLog(change_log: ChangeLogSchema, db: Session = Depends(get_db)):
    return base_result.success(crud.createChangeLog(db, change_log))

@board_router.put("/changelog/{change_log_pk}", response_model=ResponseData, description="게시글 변경 이력 수정", summary="게시글 변경 이력 수정")
async def updateChangeLog(change_log_pk: int, update_change_log: ChangeLogSchema, db: Session = Depends(get_db)):
    db_changelog = crud.getChangeLog(db, change_log_pk=change_log_pk)
    if db_changelog is None:
        return base_result.not_found()
    return base_result.success(crud.updateChangeLog(db, change_log_pk, update_change_log))

@board_router.delete("/changelog/{change_log_pk}", response_model=ResponseData, description="게시글 변경 이력 삭제", summary="게시글 변경 이력 삭제")
async def deleteChangeLog(change_log_pk: int, db: Session = Depends(get_db)):
    db_changelog = crud.getChangeLog(db, change_log_pk=change_log_pk)
    if db_changelog is None:
        return base_result.not_found()
    return base_result.success(crud.deleteChangeLog(db, change_log_pk))

@board_router.get("/tag/", response_model=ResponseData, description="게시글 태그 목록 조회", summary="게시글 태그 목록 조회")
async def readBoardTagList(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    board_tag_list = crud.getBoardTagList(db, skip=skip, limit=limit)
    return base_result.success(board_tag_list)

@board_router.get("/tag/{board_tag_pk}", response_model=ResponseData, description="특정 게시글 태그 조회", summary="특정 게시글 태그 조회")
async def readBoardTag(board_tag_pk: int, db: Session = Depends(get_db)):
    db_board_tag = crud.getBoardTag(db, board_tag_pk=board_tag_pk)
    if db_board_tag is None:
        return base_result.not_found()
    return base_result.success(db_board_tag)

@board_router.post("/tag/", response_model=ResponseData, description="게시글 태그 생성", summary="게시글 태그 생성")
async def createBoardTag(board_tag: BoardTagSchema, db: Session = Depends(get_db)):
    return base_result.success(crud.createBoardTag(db, board_tag))

@board_router.put("/tag/{board_tag_pk}", response_model=ResponseData, description="게시글 태그 수정", summary="게시글 태그 수정")
async def updateBoardTag(board_tag_pk: int, update_board_tag: BoardTagSchema, db: Session = Depends(get_db)):
    db_board_tag = crud.getBoardTag(db, board_tag_pk=board_tag_pk)
    if db_board_tag is None:
        return base_result.not_found()
    return base_result.success(crud.updateBoardTag(db, board_tag_pk, update_board_tag))

@board_router.delete("/tag/{board_tag_pk}", response_model=ResponseData, description="게시글 태그 삭제", summary="게시글 태그 삭제")
async def deleteBoardTag(board_tag_pk: int, db: Session = Depends(get_db)):
    db_board_tag = crud.getBoardTag(db, board_tag_pk=board_tag_pk)
    if db_board_tag is None:
        return base_result.not_found()
    return base_result.success(crud.deleteBoardTag(db, board_tag_pk))

@board_router.get("/category/", response_model=ResponseData, description="게시글 카테고리 목록 조회", summary="게시글 카테고리 목록 조회")
async def readCategoryList(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    board_category_list = crud.getCategoryList(db, skip=skip, limit=limit)
    return base_result.success(board_category_list)

@board_router.get("/category/{category_pk}", response_model=ResponseData, description="특정 카테고리 조회", summary="특정 카테고리 조회")
async def readCategory(category_pk: int, db: Session = Depends(get_db)):
    db_board_category = crud.getCategory(db, category_pk=category_pk)
    if db_board_category is None:
        return base_result.not_found()
    return base_result.success(db_board_category)

@board_router.post("/category/", response_model=ResponseData, description="게시글 카테고리 생성", summary="게시글 카테고리 생성")
async def createCategory(category: CategorySchema, db: Session = Depends(get_db)):
    return base_result.success(crud.createCategory(db, category))

@board_router.put("/category/{category_pk}", response_model=ResponseData, description="게시글 카테고리 수정", summary="게시글 카테고리 수정")
async def updateCategory(category_pk: int, update_category: CategorySchema, db: Session = Depends(get_db)):
    db_board_category = crud.getCategory(db, category_pk=category_pk)
    if db_board_category is None:
        return base_result.not_found()
    return base_result.success(crud.updateCategory(db, category_pk, update_category))

@board_router.delete("/category/{category_pk}", response_model=ResponseData, description="게시글 카테고리 삭제", summary="게시글 카테고리 삭제")
async def deleteCategory(category_pk: int, db: Session = Depends(get_db)):
    db_board_category = crud.getCategory(db, category_pk=category_pk)
    if db_board_category is None:
        return base_result.not_found()
    return base_result.success(crud.deleteCategory(db, category_pk))

@board_router.get("/opinion/", response_model=ResponseData, description="게시글 의견 목록 조회", summary="게시글 의견 목록 조회")
async def readOpinionList(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    board_opinion_list = crud.getOpinionList(db, skip=skip, limit=limit)
    return base_result.success(board_opinion_list)

@board_router.get("/opinion/{opinion_pk}", response_model=ResponseData, description="특정 의견 조회", summary="특정 의견 조회")
async def readOpinion(opinion_pk: int, db: Session = Depends(get_db)):
    db_board_opinion = crud.getOpinion(db, opinion_pk=opinion_pk)
    if db_board_opinion is None:
        return base_result.not_found()
    return base_result.success(db_board_opinion)

@board_router.post("/opinion/", response_model=ResponseData, description="게시글 의견 생성", summary="게시글 의견 생성")
async def createOpinion(opinion: OpinionSchema, db: Session = Depends(get_db)):
    return base_result.success(crud.createOpinion(db, opinion))

@board_router.put("/opinion/{opinion_pk}", response_model=ResponseData, description="게시글 의견 수정", summary="게시글 의견 수정")
async def updateOpinion(opinion_pk: int, update_opinion: OpinionSchema, db: Session = Depends(get_db)):
    db_board_opinion = crud.getOpinion(db, opinion_pk=opinion_pk)
    if db_board_opinion is None:
        return base_result.not_found()
    return base_result.success(crud.updateOpinion(db, opinion_pk, update_opinion))

@board_router.delete("/opinion/{opinion_pk}", response_model=ResponseData, description="게시글 의견 삭제", summary="게시글 의견 삭제")
async def deleteOpinion(opinion_pk: int, db: Session = Depends(get_db)):
    db_board_opinion = crud.getOpinion(db, opinion_pk=opinion_pk)
    if db_board_opinion is None:
        return base_result.not_found()
    return base_result.success(crud.deleteOpinion(db, opinion_pk))

@board_router.get("/spamword/", response_model=ResponseData, description="스팸 단어 목록 조회", summary="스팸 단어 목록 조회")
async def readSpamWordList(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    spam_word_list = crud.getSpamWordList(db, skip=skip, limit=limit)
    return base_result.success(spam_word_list)

@board_router.get("/spamword/{spam_word_pk}", response_model=ResponseData, description="특정 스팸 단어 조회", summary="특정 스팸 단어 조회")
async def readSpamWord(spam_word_pk: int, db: Session = Depends(get_db)):
    db_spam_word = crud.getSpamWord(db, spam_word_pk=spam_word_pk)
    if db_spam_word is None:
        return base_result.not_found()
    return base_result.success(db_spam_word)

@board_router.post("/spamword/", response_model=ResponseData, description="스팸 단어 생성", summary="스팸 단어 생성")
async def createSpamWord(spam_word: SpamWordSchema, db: Session = Depends(get_db)):
    return base_result.success(crud.createSpamWord(db, spam_word))

@board_router.put("/spamword/{spam_word_pk}", response_model=ResponseData, description="스팸 단어 수정", summary="스팸 단어 수정")
async def updateSpamWord(spam_word_pk: int, update_spam_word: SpamWordSchema, db: Session = Depends(get_db)):
    db_spam_word = crud.getSpamWord(db, spam_word_pk=spam_word_pk)
    if db_spam_word is None:
        return base_result.not_found()
    return base_result.success(crud.updateSpamWord(db, spam_word_pk, update_spam_word))

@board_router.delete("/spamword/{spam_word_pk}", response_model=ResponseData, description="스팸 단어 삭제", summary="스팸 단어 삭제")
async def deleteSpamWord(spam_word_pk: int, db: Session = Depends(get_db)):
    db_spam_word = crud.getSpamWord(db, spam_word_pk=spam_word_pk)
    if db_spam_word is None:
        return base_result.not_found()
    return base_result.success(crud.deleteSpamWord(db, spam_word_pk))