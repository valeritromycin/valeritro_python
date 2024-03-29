MORSE = {'.-': 'a', '-...': 'b', '-.-.': 'c',
         '-..': 'd', '.': 'e', '..-.': 'f',
         '--.': 'g', '....': 'h', '..': 'i',
         '.---': 'j', '-.-': 'k', '.-..': 'l',
         '--': 'm', '-.': 'n', '---': 'o',
         '.--.': 'p', '--.-': 'q', '.-.': 'r',
         '...': 's', '-': 't', '..-': 'u',
         '...-': 'v', '.--': 'w', '-..-': 'x',
         '-.--': 'y', '--..': 'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
         }


def morse_encode(str):
    temp_str = ' '.join(str.lower())
    for (key, value) in MORSE.items():
        temp_str = temp_str.replace(value, key)
    return temp_str


str = input('Введите строку латинскими буквами: ')
print(morse_encode(str))


def morse_decode(str):
     temp_morse_str = str.split(" ")
     result = []
     for m_char in temp_morse_str:
         decode_char = MORSE[m_char] if m_char else " "
         result.append(decode_char)
     return "".join(result).capitalize()


str = input('Введите шифр: ')
print(morse_decode(str))

