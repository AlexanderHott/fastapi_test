from fastapi import FastAPI
import typing as t
from pydantic import BaseModel
import uvicorn

app: FastAPI = FastAPI()


class Blog(BaseModel):
    """Blog dataclass"""

    title: str
    body: str
    published: t.Optional[bool]


@app.get("/blog")
def index(limit: int = 10, pub: bool = True, sort: t.Optional[str] = None):
    return {
        "data": f"{limit} {'published' if pub else 'unpublished'} blogs from the db"
    }


@app.get("/blog/unpublished")
def unpublished():
    return {"data": "unpublished"}


@app.get("/blog/{id_}")
def blog(id_: int):
    return {"data": f"{id_}"}


@app.get("/blog/{id_}/comments")
def blog_comments(id_: int, limit=10):
    return {"data": {f"{id_}/comments": ["1", "2", "3"]}}


@app.post("/blog")
def blog_post(blog: Blog):
    return {"data": blog}


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9001)
