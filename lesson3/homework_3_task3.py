user_input = input("введите слова через пробел\n>>>")
user_words = user_input.split(" ")

num = 0
words_amount = len(user_words)
max_word_len = 10
column_len = len(str(words_amount))
while num < words_amount:
    print(f"{num + 1:>{column_len}}: {user_words[num][:max_word_len]:^{max_word_len}}")
    num += 1