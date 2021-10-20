some_list = [1, 3, 4, 5, 6, 3, 1, 4]


def find_one_func(numbers_list):
    for number in numbers_list:
        if numbers_list.count(number) == 1:  # функция возвращает количество элементов в списке
            yield number


result = list(find_one_func(some_list))  # необходимо представить массив чисел
print(result)