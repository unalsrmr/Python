class Hayvan:
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas

    def ses_cikar(self):
        return "Hayvan ses çıkarıyor..."

class Kedi(Hayvan):
    def __init__(self, isim, yas, cins):
        super().__init__(isim, yas)
        self.cins = cins

    def ses_cikar(self):
        return "Miyav!"



class Arac:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    def bilgileri_goster(self):
        return f"{self.marka} {self.model}"

class Araba(Arac):
    def __init__(self, marka, model, kapi_sayisi):
        super().__init__(marka, model)
        self.kapi_sayisi = kapi_sayisi

    def bilgileri_goster(self):
        return f"{self.marka} {self.model} - {self.kapi_sayisi} kapı"

class ElektrikliAraba(Araba):
    def __init__(self, marka, model, kapi_sayisi, batarya_kapasitesi):
        super().__init__(marka, model, kapi_sayisi)
        self.batarya_kapasitesi = batarya_kapasitesi

    def bilgileri_goster(self):
        return f"{self.marka} {self.model} - {self.kapi_sayisi} kapı - {self.batarya_kapasitesi} kWh batarya"



def main():
    kedi1 = Kedi("Minnak", 2, "Tekir")
    print(f"{kedi1.isim} ({kedi1.cins}) {kedi1.yas} yaşında.")
    print(kedi1.ses_cikar())
    tesla = ElektrikliAraba("Tesla", "Model 3", 4, 75)
    print(tesla.bilgileri_goster())

main()
