import typing as t

from fastapi import Depends, FastAPI, HTTPException, Response, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from . import models, schemas
from .database import SessionLocal, engine


app = FastAPI()

models.Base.metadata.create_all(engine)


def get_db_session() -> t.Generator[sessionmaker, None, None]:
    db: sessionmaker = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/blog", status_code=status.HTTP_201_CREATED)
def blog_post(blog: schemas.Blog, db: Session = Depends(get_db_session)):
    new_blog = models.Blog(**blog.dict())
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return {"data": new_blog}


@app.get("/blog")
def blog_get(db: Session = Depends(get_db_session)):
    if blogs := db.query(models.Blog).all():
        return blogs
    else:
        return JSONResponse(
            content={"error": "No blogs found"}, status_code=status.HTTP_404_NOT_FOUND
        )


@app.get("/blog/{id_}", status_code=200)
def blog_id_get(id_: int, response: Response, db: Session = Depends(get_db_session)):
    if blog := db.query(models.Blog).filter(models.Blog.id == id_).first():
        return blog
    else:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"error": f"Blog with id {id_} is not found"}
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id_} is not found",
        )


# 1:53:50
