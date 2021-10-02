from sqlalchemy import Column, Integer, String
from .database import Base


class Blog(Base):
    """Databse Model for blogs"""

    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
