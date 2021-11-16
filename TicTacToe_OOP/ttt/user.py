from .mixins import GamerNameMixin, GamerStepMixin


class Gamer(GamerNameMixin, GamerStepMixin):
    _is_human = False

    def __init__(self, symbol, name=None):
        if name:
            self.name = name
        else:
            self.name = self._get_name()
        self.symbol = symbol

    def __str__(self):
        return self.name


class HumanGamer(Gamer):
    _is_human = True