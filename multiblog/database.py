from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from multiblog import tables
from multiblog.populate_db import generate_fullname


class DataBase:

    def __init__(self, db_url):
        engine = create_engine(db_url, echo=True)
        tables.Base.metadata.create_all(bind=engine)
        self.maker = sessionmaker(bind=engine)

    def populate_db(self):
        session = self.maker()
        data = generate_fullname()
        session.add_all(data)
        session.commit()
        session.close()


if __name__ == '__main__':
    db_url = "sqlite:///db.multiblog"
    db = DataBase(db_url)
    db.populate_db()
    print(1)