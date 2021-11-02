import sys
from itertools import cycle

from board import get_board, board_match, print_board
from steps import user_step
from users import ask_mode, create_users, MODES


def game_init() -> dict:
    print("Добро пожаловать в Игру Крестики Нолики")
    mode = None
    try:
        argv_mode = sys.argv[2]
        if argv_mode.upper() in MODES:
            mode = argv_mode
    except IndexError:
        pass
    if not mode:
        mode = ask_mode()

    name = sys.argv[3]

    return {
        "users": create_users(mode),
        "board": get_board(3),
    }


def game_end(step_num, winner):
    result_result_str = f'победил игрок {winner["name"]}' if winner else 'произошла ничья'
    result_to_print = f"На {step_num} ходу, {result_result_str}"
    print(result_to_print)
    variants = ("Y", "N")
    while True:
        user_input = input(f"Реванш? {'/'.join(variants)}").upper()
        if user_input in variants:
            return user_input == variants[0]
        print("Неверный ввод, повторите")


def game_cycle(users: list[dict, ...], board: list[list]):
    winner = None
    step_num = None
    steps = set()
    for step_num, user in enumerate(cycle(users), 1):
        user["all_steps"] = steps
        print(f"Ход Игрока: {user['name']}")
        print_board(board)
        step = user_step(user, board)
        user["steps"].append(step)
        steps.add(step)
        if board_match(board):
            winner = user
            break
        if step_num > 8:
            break
    return step_num, winner
