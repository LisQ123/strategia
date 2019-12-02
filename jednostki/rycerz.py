from wojownik import Wojownik


class Rycerz(Wojownik):
    def __init__(self):
        super().__init__()
        self.zycie = 60

    def atakuj(self):
        print('Rycerze: Machnalem mieczem!')
        self._doswiadczenie += 0.3
