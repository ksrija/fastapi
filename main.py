from fastapi import FastAPI

app= FastAPI()

@app.get("/")
def index():
    return {"data":{"name":"John"}}

@app.get("/blog/unpublished")
def unpublished():
    return {"commments":"Unpublished comments"}


@app.get("/blog/{id}")
def show(id: int):
    "Fetch blog with id = id"
    return {"data":id}

@app.get("/blog/{id}/comments")
def comments(id: int):
    "Fetch comments of id=id"

    return {"comments":{"This is wonderful!","That is amazing."}}


