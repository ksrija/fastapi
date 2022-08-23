# from lib2to3.pytree import Base
# from turtle import title
from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas, model
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List

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
    new_blog = model.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

    # conn.local.user.insert_one(dict(request))
    # return conn.local.user.find()


@app.get("/blog", status_code=status.HTTP_201_CREATED, response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db)):
    blogs = db.query(model.Blog).all()
    return blogs

    # blogs = schemas.Blog(conn.local.user.find())
    # return blogs


# response model we will get according to the type of schema defined.
@app.get("/blog/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(id, db: Session = Depends(get_db)):
    blog = db.query(model.Blog).filter(model.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")

    return blog


@app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):
    blog = db.query(model.Blog).filter(model.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found.")
    blog.delete(synchronize_session=False)
    db.commit()
    return "Done"


@app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(model.Blog).filter(model.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found.")
    blog.update({"title": request.title, "body": request.body})
    db.commit()
    return "Updated"


@app.post("/users")
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = model.User(
        name=request.name, email=request.email, password=request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
