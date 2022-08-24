from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas, model, user
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List
from .db import collection_name, collection_name_1
from bson import ObjectId
app = FastAPI()

# this is the line responsible fo creating the database
# if the table is not there it is gonna create one a
# and if there is one then it is not when the server is running.
model.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/blog", status_code=status.HTTP_201_CREATED)
def posts(request: schemas.Blog, db: Session = Depends(get_db)):
    _id = collection_name.insert_one(dict(request))
    return dict(request)


@app.get("/blog", status_code=status.HTTP_201_CREATED, response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db)):

    blogs = list(
        collection_name.find())
    return blogs


# response model we will get according to the type of schema defined.
@app.get("/blog/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(id, db: Session = Depends(get_db)):
    blog = collection_name.find_one({"_id": ObjectId(id)})
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")
    return blog


@app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):
    blog = collection_name.find_one({"_id": ObjectId(id)})
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found.")

    blog = collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return "Done"


@app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = collection_name.find_one({"_id": ObjectId(id)})
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found.")
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(request)
    })
    return "Updated"


@app.post("/users")
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    _id = collection_name_1.insert_one(dict(request))
    return dict(request)
