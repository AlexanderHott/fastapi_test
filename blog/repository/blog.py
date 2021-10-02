from sqlalchemy.orm.session import Session
from fastapi import Depends, HTTPException, status
from blog import models

from blog.database import get_db_session


def blog_get(db: Session = Depends(get_db_session)):
    if blogs := db.query(models.Blog).all():
        return blogs
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="No blogs found"
        )
