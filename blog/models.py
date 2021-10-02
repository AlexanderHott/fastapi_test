from sqlalchemy import Column, Integer, String, ForeignKey 
from sqlalchemy.orm import relationship
# from sqlalchemy.sql.schema import ForeignKey

from .database import Base


class Blog(Base):
    """Databse Model for blogs"""

    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    creator = relationship("User", back_populates="blogs")


class User(Base):
    """Database model for users"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = relationship("Blog", back_populates="creator")
