from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()


@app.get("/")
def index():
    return {"data": {"name": "John"}}


@app.get("/blog")
def get_blogs(limit=10, published: bool = True, sort: Optional[str] = None):
    """Get 10 blogs."""
    if published:
        return {"data": f"{limit} published blogs from the database."}
    else:
        return {"data": f"{limit} blogs from the database."}


@app.get("/blog/unpublished")
def unpublished():
    return {"commments": "Unpublished comments"}


@app.get("/blog/{id}")
def show(id: int):
    "Fetch blog with id = id"
    return {"data": id}


@app.get("/blog/{id}/comments")
def comments(id: int, limit=10):
    "Fetch comments of id=id"

    return {"comments": {"This is wonderful!", "That is amazing."}, "limit": limit}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post("/blog")
def posts(blog: Blog):
    return {"data": f"Blog has been created with title {blog.title}"}

# Mainly for debugging purposes
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)
