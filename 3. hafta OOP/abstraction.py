from abc import ABC, abstractmethod

class Sekil(ABC):  # Soyut sınıf
    @abstractmethod
    def alan(self):
        pass
    
    @abstractmethod
    def cevre(self):
        pass

class Kare(Sekil):
    def __init__(self, kenar):
        self.kenar = kenar

    def alan(self):
        return self.kenar ** 2

    def cevre(self):
        return 4 * self.kenar

class Daire(Sekil):
    def __init__(self, yaricap):
        self.yaricap = yaricap

    def alan(self):
        return 3.14 * self.yaricap ** 2

    def cevre(self):
        return 2 * 3.14 * self.yaricap

sekiller = [Kare(4), Daire(3)]

for sekil in sekiller:
    print(f"Alan: {sekil.alan()}, Çevre: {sekil.cevre()}")
