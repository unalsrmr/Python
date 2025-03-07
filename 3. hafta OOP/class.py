class Araba:
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil

    def bilgileri_goster(self):
        return f"{self.yil} model {self.marka} {self.model}"

class Kitap:
    def __init__(self, ad, yazar, sayfa_sayisi):
        self.ad = ad
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi

    def bilgileri_goster(self):
        return f"{self.ad} - {self.yazar} ({self.sayfa_sayisi} sayfa)"

class Telefon:
    def __init__(self, marka, model, fiyat):
        self.marka = marka
        self.model = model
        self.fiyat = fiyat

    def bilgileri_goster(self):
        return f"{self.marka} {self.model} - {self.fiyat} TL"

def main():
    araba1 = Araba("Toyota", "Corolla", 2022)
    print(araba1.bilgileri_goster())
    kitap1 = Kitap("Suç ve Ceza", "Fyodor Dostoyevski", 671)
    kitap2 = Kitap("1984", "George Orwell", 328)

    print(kitap1.bilgileri_goster())
    print(kitap2.bilgileri_goster())
    telefon1 = Telefon("Apple", "iPhone 13", 45000)
    telefon2 = Telefon("Samsung", "Galaxy S23", 38000)

    print(telefon1.bilgileri_goster())
    print(telefon2.bilgileri_goster())

main()