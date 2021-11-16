from itertools import cycle

from .game_result import GameResult


class TicTacToe:

    def __init__(self, users: tuple, board):
        self.users = users
        self.board = board

    def run(self):
        for step_num, user in enumerate(cycle(self.users)):
            print(f"Ход игрока {user} с символом {user.symbol}")
            print(self.board)
            # self.board.print_board()
            self.__game_step(user)
            if self.board.chek_board():
                return GameResult(step_num, user)
            if step_num == (self.board.size() ** 2):
                return GameResult(step_num, None)

    def __game_step(self, user):
        while True:
            step = user.get_step(self.board.free_cells())
            try:
                self.board.add_step(step, user.symbol)
            except ValueError:
                print("Неверные координаты, повторите ввод")
                continue
            break