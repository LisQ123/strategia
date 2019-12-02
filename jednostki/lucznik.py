from wojownik import Wojownik


class Lucznik(Wojownik):
    def __init__(self):
        super().__init__()
        self.zycie = 40
        self.strzaly = 10

    def atakuj(self):
        if self.strzaly > 0:
            print('Lucznik: Wypuscilem strzale!')
            self.strzaly -= 1
            self._doswiadczenie += 0.4
        else:
            print('Lucznik: Nie mam strzal! Nie moge atakowac!')
