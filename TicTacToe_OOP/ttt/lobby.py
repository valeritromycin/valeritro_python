import sys

from .board import Board
from .game import TicTacToe
from .user import HumanGamer, Gamer


class Lobby:
    __commands_keys = (
        '-u1',
        '-u2',
        '-mode',
    )
    __modes = {
        "COMP": (lambda name: HumanGamer("X", name), lambda name: Gamer("O", name)),
        "USER": (lambda name: HumanGamer("X", name), lambda name: HumanGamer("O", name)),
        "default": "COMP"
    }

    def __init__(self, users_names, mode, board_size=3, game_cls=TicTacToe):
        self.mode = mode
        self.users = tuple(
            user_cls(name) for name, user_cls in zip(
                users_names, self.__modes.get(self.mode, self.__modes[self.__modes["default"]])
            )
        )
        self.board = Board(board_size)
        self.game = game_cls(self.users, self.board)

    @classmethod
    def new_game(cls):
        commands = cls.__get_commands()
        return cls((commands.get('-u1'), commands.get('-u2')), commands['-mode'])

    @classmethod
    def __get_commands(cls):
        result = {}
        if "help" in sys.argv:
            cls.__help()
            sys.exit(0)
        else:
            for key in cls.__commands_keys:
                if key in sys.argv:
                    try:
                        result[key] = sys.argv[sys.argv.index(key) + 1]
                    except IndexError:
                        print("Неверный Ввод аргументов")
                        cls.__help()
                        sys.exit(1)
        return result

    @staticmethod
    def __help():
        print("help text")

    def main(self):
        game_result = self.game.run()
        print(game_result)