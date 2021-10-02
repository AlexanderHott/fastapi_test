import sqlalchemy
from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm.session import Session, sessionmaker

from blog import models, schemas
from blog.database import get_db_session
from blog.hashing import Hash

router = APIRouter()


@router.post("/user", response_model=schemas.EUUser, tags=["users"])
def user_post(request: schemas.User, db: Session = Depends(get_db_session)):
    hashed_password = Hash.bcrypt(request.password)
    new_user = models.User(**{**request.dict(), "password": hashed_password})

    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except sqlalchemy.exc.IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"UNIQUE constraint failed"
        )
    return new_user


@router.get("/user/{id_}", response_model=schemas.EUUser, tags=["users"])
def user_get(id_: int, db: Session = Depends(get_db_session)):
    if user := db.query(models.User).filter(models.User.id == id_).first():
        return user
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id_} not found",
        )
