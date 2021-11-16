import random

from .constants import BOT_NAMES


class GamerNameMixin:

    def _get_name(self):
        if self._is_human:
            return self.__ask_human_name()
        return self.__get_bot_name()

    @staticmethod
    def __ask_human_name():
        return input("Введите ваше имя")

    @staticmethod
    def __get_bot_name():
        return random.choice(BOT_NAMES)


class GamerStepMixin:

    def get_step(self, free_cells):
        if self._is_human:
            step = self.__human_step()
        else:
            step = self.__bot_step(free_cells)
        return step

    @staticmethod
    def __bot_step(free_cells: tuple):
        return random.choice(free_cells)

    @staticmethod
    def __human_step():
        while True:
            result = []
            input_step = input("Введите координаты хода через пробел\n")
            steps = input_step.split(" ")
            try:
                if len(steps) != 2:
                    raise ValueError
                for itm in steps:
                    result.append(int(itm))
            except ValueError:
                print("Ошибка ввода, повторите")
                continue
            return tuple(result)