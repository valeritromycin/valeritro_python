from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
)


Base = declarative_base()


class Blogs(Base):
    __table_name__ = 'blogs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    blog_name = Column(String(144), unique=False)


class Authors(Base):
    __table_name__ = 'authors'
    id = Column(Integer, primary_key=True, autoincrement=True)
    author_name = Column(String(144), unique=False)
    blog_id = Column(Integer, ForeignKey='blogs.id', nullable=True)


class Publications(Base):
    __table_name__ = 'publications'
    id = Column(Integer, primary_key=True, autoincrement=True)
    post_title = Column(String(144), unique=False)
    post_date = Column(DateTime, unique=False)


class Tags(Base):
    __table_name__ = 'tags'
    id = Column(Integer, primary_key=True, autoincrement=True)
    tag_title = Column(String(32), unique=True)

