from datetime import datetime
from board import get_board
from game import game_init, game_cycle, game_end


def main():
    game_vars = game_init()
    end_result = True
    while end_result:
        result_game = game_cycle(**game_vars)
        end_result = game_end(*result_game)
        if end_result:
            game_vars["board"] = get_board(3)

def log_start():
    log = open("log.py", "w", encoding = "UTF-8")
    log.write(f'Игра начата {str(datetime.now())}')
    log.close()


print(log_start())


if __name__ == '__main__':
    main()
