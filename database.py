from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# import contextlib


# 데이터베이스 접속 주소
SQLALCHEMY_DATABASE_URL = "sqlite:///./myapi.db"
# sqlite:///./myapi.db는 sqlite3 데이터베이스의 파일을 의미하며 프로젝트 루트 디렉터리에 저장한다는 의미

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# @contextlib.contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

