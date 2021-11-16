from .templates import USER_WINNER_TEMPLATE, DRAW_WINNER_TEMPLATE


class GameResult:

    def __init__(self, step_num, user):
        self.step_num = step_num
        self.user = user

    def __str_winner(self):
        return USER_WINNER_TEMPLATE.format(user=self.user, step_num=self.step_num)

    def __str_draw(self):
        return DRAW_WINNER_TEMPLATE.format(step_num=self.step_num)

    def __str__(self):
        if self.user:
            return self.__str_winner()
        return self.__str_draw()