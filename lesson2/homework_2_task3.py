numbers = [44, 22, 54, 87, 345, 912, 654, 18, 33, 76, 11]
even = []
odd = []

some_tuple = (even, odd)

some_tuple[numbers[0] % 2].append(numbers[0])
some_tuple[numbers[1] % 2].append(numbers[1])
some_tuple[numbers[2] % 2].append(numbers[2])
some_tuple[numbers[3] % 2].append(numbers[3])
some_tuple[numbers[4] % 2].append(numbers[4])
some_tuple[numbers[5] % 2].append(numbers[5])
some_tuple[numbers[6] % 2].append(numbers[6])
some_tuple[numbers[7] % 2].append(numbers[7])
some_tuple[numbers[8] % 2].append(numbers[8])
some_tuple[numbers[9] % 2].append(numbers[9])
some_tuple[numbers[10] % 2].append(numbers[10])

print(even)
print(odd)