from collections import defaultdict
from itertools import chain


class Board:

    def __init__(self, size):
        self.__size = size
        self.done_steps = defaultdict(set)

    def size(self):
        return self.__size

    def get_win_variants(self):
        variants_diagonal = (
            ((i, j) for i, j in zip(range(self.__size), range(self.__size - 1, -1, -1))),
            ((i, i) for i in range(self.__size)),
        )

        for variant in variants_diagonal:
            yield variant

        variants = (
            (((i, j) for j in range(self.__size)) for i in range(self.__size)),
            (((j, i) for j in range(self.__size)) for i in range(self.__size)),
        )
        for itm in variants:
            yield from itm

    def print_board(self):
        print(self)

    def add_step(self, step: tuple[int, int], user):
        if (
                all(map(lambda x: 0 <= x < self.__size, step))
                and (not any(map(lambda user_steps: step in user_steps, self.done_steps.values())))
        ):
            self.done_steps[user].add(step)
        else:
            raise ValueError("Сюда ходить нельзя")

    def chek_board(self):
        variants = ((wl, usr, usr_st) for usr, usr_st in self.done_steps.items() for wl in self.get_win_variants())
        for win_line, user, user_steps in variants:
            if not set(win_line).difference(user_steps):
                return user
        return None

    def free_cells(self):
        all_steps = {(i, j) for i in range(self.__size) for j in range(self.__size)}
        return tuple(all_steps.difference({itm for itm in chain(*self.done_steps.values())}))

    def __str__(self):
        board_view = [[0 for _ in range(self.__size)] for _ in range(self.__size)]
        for user, steps in self.done_steps.items():
            for step in steps:
                board_view[step[0]][step[1]] = user
        title_row = f'##{"#".join(map(str, range(len(board_view))))}#'
        str_rows = "\n".join(map(lambda itm: f"{itm[0]}#{'|'.join(map(str, itm[1]))}#", enumerate(board_view)))
        return f"{title_row}\n{str_rows}\n{'#' * len(title_row)}"