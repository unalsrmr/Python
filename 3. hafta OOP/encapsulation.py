class BankaHesabi:
    def __init__(self, hesap_sahibi, bakiye):
        self.hesap_sahibi = hesap_sahibi
        self.__bakiye = bakiye  # __ olursa başta private olur

    def bakiye_goster(self):
        return f"{self.hesap_sahibi} bakiyesi: {self.__bakiye} TL"

    def para_cek(self, miktar):
        if miktar <= self.__bakiye:
            self.__bakiye -= miktar
            return f"{miktar} TL çekildi. Yeni bakiye: {self.__bakiye} TL"
        else:
            return "Yetersiz bakiye!"

class Calisan:
    def __init__(self, isim, maas):
        self.isim = isim  #public değişken
        self.__maas = maas  #private değişken

    def maas_goster(self):#getter
        return f"{self.isim} maaşı: {self.__maas} TL"

    def maas_guncelle(self, yeni_maas):#setter
        if yeni_maas > 0:
            self.__maas = yeni_maas
            return f"{self.isim} yeni maaşı: {self.__maas} TL"
        else:
            return "Geçersiz maaş değeri!"



def main():
    hesap = BankaHesabi("Ahmet", 5000)
    print(hesap.bakiye_goster())
    print(hesap.para_cek(1000))
    calisan1 = Calisan("Zeynep", 15000)
    print(calisan1.maas_goster())
    print(calisan1.maas_guncelle(18000))
main()