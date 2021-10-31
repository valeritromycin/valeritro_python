"""
Игра Крестики нолики
"""
"""
Правила игры:
Игровое поле 3х3
участвуют 2 игрока
игроки ходят поочереди
каждый игрок имеет индивидуальный символ который ставит на свободную ячейку игрового поля
Победитель определяется по следующим правилам:
символ игрока заполняет горизонталь, вертикаль или диагональ

возможный исход игры когда нет победителя
"""
# TODO: Играть с компуктером
# TODO: Игровое поле в виде Матрицы 3на3 не изменяемо.
# TODO: Ячейка игрового поля будет изменяться,
"""(
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
)"""


interface_string = {
    "rules": "",
    "hello": "Здравствуй игрок",
    "enter_name": "Игрок #{user_number}: Введите свое имя",
    "game_type": "С кем вы желаете играть {variants}",
    "ask_step": "Ход #{step_number} игрока {name}",
    "win": "Победил игрок {name} на ходу #{step_number}",
    "new_game": "Желаете начать новую игру? {variants}",
    "draw": "Ничья победителей нет"
}

template_variants = {
    "game_type": lambda template, **kwargs: template.format(variants=("U", "C")),
    "ask_step": lambda template, **kwargs: template.format(**kwargs),
    "win": lambda template, **kwargs: template.format(**kwargs),
    "new_game": lambda template, **kwargs: template.format(variants=("Y", "N")),
    "enter_name": lambda template, **kwargs: template.format(**kwargs),
}

game_type = {
    "U": lambda x: " ",
    "C": lambda x: " "
}


def user_interface(template_name, **template_vars):
    if template_name in template_variants:
        ask_str = template_variants[template_name](interface_string[template_name], **template_vars)
        user_input = input(ask_str)
        return user_input
    else:
        print(interface_string[template_name])



