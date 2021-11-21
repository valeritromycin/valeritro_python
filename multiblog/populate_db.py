import random
from tables import Author, Blog


NAMES = [
    'Raeve',
    'Frey',
    'Tyra',
    'Melori',
    'Rayna',
    'Del',
    'Kestria',
    'Raia',
    'Echo',
    'Georgios'
]

SURNAMES = [
    'Pollo',
    'Zalie',
    'Lakkena',
    'Famir',
    'Carwel',
    'Pollo',
    'Zalie',
    'Lakkena',
    'Famir',
    'Carwel',
]

size = 100


def generate_fullname():
    add_list = []
    for i in range(size):
        name = random.choice(NAMES)
        surname = random.choice(SURNAMES)
        blog_name = f'{name} {surname}'
        blog = Blog(blog_name=blog_name)
        author = Author(author_name=name, author_surname=surname, blog_id=blog.id)
        add_list.append(blog)
        add_list.append(author)
    return add_list


generate_fullname()