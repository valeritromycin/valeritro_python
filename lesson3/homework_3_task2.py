user_month = int(input('Введите месяц года в виде числа: '))
seasons = (
    'зима',
    'весна',
    'лето',
    'осень'
)

if 0 < user_month <= 2 or user_month == 12:
    print(seasons[0])
elif 3 <= user_month <= 5:
    print(seasons[1])
elif 6 <= user_month <= 8:
    print(seasons[2])
elif 9 <= user_month <= 11:
    print(seasons[3])
else:
    print('Ошибка ввода: такого месяца не существует')
