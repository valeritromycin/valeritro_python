import random

from tables import Author, Blog


NAMES = [
    'Harry',
    'Hermione',
    'Ron',
    'Luna',
    'Jinny',
    'Nevill',
    'Severus',
    'Sirius',
    'James',
    'Draco'
]

SURNAMES = [
    'Ardonia',
    'Vasko',
    'Jordinjo',
    'Partiallo',
    'Nukirt',
    'Pollo',
    'Zalie',
    'Lakkena',
    'Famir',
    'Carwel',
]



size = 100


def generate_fullnames():
    author_list = []
    blog_list = []
    for i in range(size):
        name = random.choice(NAMES)
        surname = random.choice(SURNAMES)
        blog_name = f'{name} {surname}'
        blog = Blog(blog_name=blog_name)
        author = Author(author_name=name, author_surname=surname, blog_id=blog.id)
        blog_list.append(blog)
        author_list.append(author)
    return zip(author_list, blog_list)
