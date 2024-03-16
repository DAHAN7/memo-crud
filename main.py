from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

class Memo(BaseModel):
    id: str
    content: str

memos = []

app = FastAPI()

@app.post("/memos")
def create_memo(memo: Memo):
    memos.append(memo)
    return '내용 추가에 성공하였습니다.'

@app.get("/memos")
def read_memo():
    return memos

@app.put("/memos/{memo_id}")
def put_memo(memo_id: str, req_memo: Memo):
    for memo in memos:
        if memo.id == memo_id:
            memo.content = req_memo.content
            return '성공'
    return '요청 실패'

@app.delete("/memos/{memo_id}")
def delete_memo(memo_id: str):
    for index, memo in enumerate(memos):
        if memo.id == memo_id:
            memos.pop(index)
            return '성공'
    return '실패'

app.mount("/", StaticFiles(directory="static", html=True), name="static")
