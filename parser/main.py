import requests
from urllib.parse import urljoin, urlparse
import re


pattern = re.compile(r"href=\"(/promo/\S+)\"")

product_pattern = re.compile(r"\"action__title\">.*</div>")


def get_page(url):
    return requests.get(url)


url = "https://magnit.ru/promo/"
response = get_page(url)

products = set()
for link in re.findall(pattern, response.text):
    base = urlparse(response.url)
    url = urljoin(response.url, link)
    if base.netloc == urlparse(url).netloc:
        if url not in products:
            product_page = get_page(url).text

            product_name_raw = re.findall(product_pattern, product_page)[0]
            product_name = product_name_raw[16:-6]
            # TODO product = Product(url=url, product_name=product_name)
            # TODO session.add(product)
            # TODO session.commit()
