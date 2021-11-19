import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from multiblog import tables


class DataBase:

    def __init__(self, db_url):
        engine = create_engine(db_url)
        tables.Base.metadata.create_all(bind=engine)
        self.maker = sessionmaker(bind=engine)


if __name__ == '__main__':
    db_url = "sqlite:///db.multiblog"
    db = DataBase(db_url)
    print(1)