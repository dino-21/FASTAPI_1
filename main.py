from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.answer import answer_router
from domain.question import question_router

app = FastAPI()

origins = [
    "http://localhost:5173",  # localhost를 허용
    "http://127.0.0.1:5173",  # 127.0.0.1도 허용
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # CORS 설정에 localhost와 127.0.0.1을 모두 허용
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.get("/hello")
# def hello():
#     return {"message": "안녕하세요 파이보"}

app.include_router(question_router.router)
app.include_router(answer_router.router)

