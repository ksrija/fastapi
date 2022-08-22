from lib2to3.pytree import Base
from fastapi import FastAPI
from . import schemas, model
from .database import engine

app = FastAPI()

# this is the line responsible fo creating the database
# if the table is not there it is gonna create one and if there is one then it is not when the server is running.
model.Base.metadata.create_all(engine)


@app.post("/blog")
def posts(request: schemas.Blog):
    return request
