user_input = input('Введите последовательность из чисел: ')
user_numbers = user_input.split(" ")
numbers_amount = len(user_numbers)
num = 1
while num < numbers_amount:
    user_numbers[num - 1], user_numbers[num] = user_numbers[num], user_numbers[num - 1]
    num += 2
print(user_numbers)
