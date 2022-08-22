from sqlalchemy import Column, Integer, String
from .database import Base

# schema of table


class blog(Base):

    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
