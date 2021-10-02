from pydantic import BaseModel


class BlogBase(BaseModel):
    """Basic blog schema for api requests"""

    title: str
    body: str


class Blog(BaseModel):
    """Relational blog schema for api requests"""

    title: str
    body: str

    class Config(object):
        orm_mode = True


class User(BaseModel):
    """User schmea"""

    name: str
    email: str
    password: str


class EUUser(BaseModel):
    """End user User schema that hides passwords"""

    name: str
    email: str
    blogs: list[Blog] = []

    class Config(object):
        orm_mode = True


class EUBlog(BaseModel):
    """End user blog schema for only showing useful information"""

    title: str
    body: str
    creator: EUUser

    class Config(object):
        """Config for end user schemas"""

        orm_mode = True
