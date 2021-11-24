import requests
from urllib.parse import urljoin, urlparse
import re
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    Integer,
    String,
    create_engine,
)
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class DataBase:

    def __init__(self, db_url):
        engine = create_engine(db_url)
        Base.metadata.create_all(bind=engine)
        self.maker = sessionmaker(bind=engine)


db = DataBase("sqlite:///db.magnit")

url = "https://magnit.ru/promo/"
pattern = re.compile(r"href=\"(/promo/\S+)\"")
product_pattern = re.compile(r"\"action__title\">.*</div>")


class Goods(Base):
    __tablename__ = 'goods'
    id = Column(Integer, primary_key=True, autoincrement=True)
    goods_link = Column(String(256), unique=True)
    goods_name = Column(String(256), unique=False)


def get_page(url):
    return requests.get(url)


response = get_page(url)
products = set()


for link in re.findall(pattern, response.text):
    base = urlparse(response.url)
    url = urljoin(response.url, link)
    if base.netloc == urlparse(url).netloc:
        if url not in products:
            goods_link = get_page(url).text
            goods_name_raw = re.findall(product_pattern, goods_link)[0]
            goods_name = goods_name_raw[16:-6]
            goods = Goods(goods_link=goods_link, goods_name=goods_name)
            db_url = "sqlite:///db.magnit"
            db = DataBase(db_url)
            session = db.maker()
            session.add(goods)
            session.commit()
            session.close()

        else:
            pass