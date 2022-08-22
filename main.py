from typing import Optional
from fastapi import FastAPI

app= FastAPI()

@app.get("/")
def index():
    return {"data":{"name":"John"}}

@app.get("/blog")
def get_blogs(limit=10 ,published: bool=True, sort: Optional[str] = None):
    '''Get 10 blogs.'''
    if published:
        return {"data":f"{limit} published blogs from the database."}
    else:
        return {"data":f"{limit} blogs from the database."}

@app.get("/blog/unpublished")
def unpublished():
    return {"commments":"Unpublished comments"}


@app.get("/blog/{id}")
def show(id: int):
    "Fetch blog with id = id"
    return {"data":id}

@app.get("/blog/{id}/comments")
def comments(id: int, limit =10):
    "Fetch comments of id=id"

    return {"comments":{"This is wonderful!","That is amazing."}, "limit": limit}


