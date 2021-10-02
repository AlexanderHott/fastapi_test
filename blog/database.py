from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import typing as t

DB_URL = "sqlite:///blog.sqlite3"
engine = create_engine(DB_URL, connect_args={"check_same_thread": False})

SessionLocal: sessionmaker = sessionmaker(
    bind=engine, autocommit=False, autoflush=False
)
Base = declarative_base()

def get_db_session() -> t.Generator[sessionmaker, None, None]:
    """Generator for acquiring database sessions"""
    db: sessionmaker = SessionLocal()
    try:
        yield db
    finally:
        db.close()

