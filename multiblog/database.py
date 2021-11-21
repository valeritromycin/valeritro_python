from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from multiblog import tables
from multiblog.populate_db import generate_fullnames


class DataBase:

    def __init__(self, db_url):
        engine = create_engine(db_url)
        tables.Base.metadata.create_all(bind=engine)
        self.maker = sessionmaker(bind=engine)

    def populate_db(self):
        session = self.maker()
        data = generate_fullnames()
        for item in data:
            blog = item[1]
            session.add(blog)
            session.flush()
            author = item[0]
            author.blog_id = blog.id
            session.add(author)
            session.flush()
        session.commit()
        session.close()


if __name__ == '__main__':
    db_url = "sqlite:///db.multiblog"
    db = DataBase(db_url)
    db.populate_db()
    print(1)