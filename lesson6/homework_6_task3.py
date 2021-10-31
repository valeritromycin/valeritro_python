some_text = "Пал, а норов худ и дух ворона лап."


def pal_check(str):
    new_str = str.replace(' ', '').replace(',', '').replace('.', '')
    new_str = new_str.lower()
    return new_str == new_str[::-1]


print(pal_check(some_text))

