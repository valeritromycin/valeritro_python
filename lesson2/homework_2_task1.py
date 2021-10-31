users = (
    {
        "name": "Jon",
        "surname": "Smith",
        "age": 6,
    },
    {
        "name": "Bill",
        "surname": "Suns",
        "age": 20,
    }
)
templates = (
    "{name} {surname} закончил школу",
    "{name} {surname} скоро пойдет в школу",
)
finaltext1 = templates[users[0]['age'] < 7].format(name = users[0]['name'], surname = users[0]['surname'])
print(finaltext1)

finaltext2 = templates[users[1]['age'] < 7].format(name = users[1]['name'], surname = users[1]['surname'])
print(finaltext2)




# solution
result = templates[users[0]["age"] < 7].format(
    name=users[0]["name"],
    surname=users[0]["surname"],
)
print(result)

result = templates[users[1]["age"] < 7].format(
    name=users[1]["name"],
    surname=users[1]["surname"],
)
print(result)

