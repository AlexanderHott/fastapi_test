from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm.session import Session


from blog import models, schemas
from blog.database import get_db_session
from ..repository import blog

router = APIRouter(prefix="/blog", tags=["Blogs"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def blog_post(blog: schemas.Blog, db: Session = Depends(get_db_session)):
    new_blog = models.Blog(**{**blog.dict(), "user_id": 1})
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return {"data": new_blog}


@router.get("/", status_code=200, response_model=list[schemas.EUBlog])
def blog_get(db: Session = Depends(get_db_session)):
    return blog.blog_get(db)

@router.get("/{id_}", status_code=200, response_model=schemas.EUBlog)
def blog_id_get(id_: int, db: Session = Depends(get_db_session)):
    if blog := db.query(models.Blog).filter(models.Blog.id == id_).first():
        return blog
    else:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"error": f"Blog with id {id_} is not found"}
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id_} not found",
        )


@router.delete("/{_id}", status_code=status.HTTP_204_NO_CONTENT)
def blog_id_delete(id_: int, db: Session = Depends(get_db_session)):
    if blog := db.query(models.Blog).filter(models.Blog.id == id_).first():
        blog.delete(synchronize_session=False)
        db.commit()
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id_} not found",
        )
    # TODO Find a way to select all blogs with `id` for update/delete


@router.put("/{id_}", status_code=status.HTTP_202_ACCEPTED)
def blog_id_update(
    id_: int, request: schemas.Blog, db: Session = Depends(get_db_session)
):
    if blog := db.query(models.Blog).filter(models.Blog.id == id_).first():
        blog.update(request.dict())
        db.commit()
        return request.dict()
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id_} not found",
        )
