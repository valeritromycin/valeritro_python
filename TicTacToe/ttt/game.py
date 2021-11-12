import sys
from itertools import cycle

from .board import get_board, board_match, print_board
from .game_logger import write_init, get_game_num, write_step, write_end_game
from .steps import user_step
from .users import ask_mode, create_users, MODES


def game_init() -> dict:
    print("Добро пожаловать в Игру Крестики Нолики")
    mode = None
    try:
        argv_mode = sys.argv[1]
        if argv_mode.upper() in MODES:
            mode = argv_mode
    except IndexError:
        pass
    if not mode:
        mode = ask_mode()
    game_num = get_game_num()
    init_data = {
        "users": create_users(mode),
        "board": get_board(3),
        "mode": mode,
        "game_num": game_num,
        "game_iter_num": 1,
    }
    write_init(init_data)
    return init_data


def game_end(step_num, winner, game_id, game_iter_num):
    result_result_str = f'победил игрок {winner["name"]}' if winner else 'произошла ничья'
    result_to_print = f"На {step_num} ходу, {result_result_str}"
    print(result_to_print)
    write_end_game(
        game_id=game_id,
        game_iter_num=game_iter_num,
        winner=winner["name"] if winner else "NO_WINNER",
        step_num=step_num
    )
    variants = ("Y", "N")
    while True:
        user_input = input(f"Реванш? {'/'.join(variants)}").upper()
        if user_input in variants:
            return user_input == variants[0]
        print("Неверный ввод, повторите")


def game_cycle(users: list[dict, ...], board: list[list], mode, game_num, game_iter_num):
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
        write_step(user, step, step_num, game_num, game_iter_num)
        if board_match(board):
            winner = user
            break
        if step_num > 8:
            break
    return step_num, winner
