class Hayvan:
    def ses_cikar(self):
        return "Bir hayvan ses çıkarıyor..."

class Kedi(Hayvan):
    def ses_cikar(self): 
        return "Miyav!"

class Kopek(Hayvan):
    def ses_cikar(self):  
        return "Hav hav!"
    
hayvanlar = [Kedi(), Kopek(), Hayvan()]

for hayvan in hayvanlar:
    print(hayvan.ses_cikar())

class HesapMakinesi:
    def topla(self, *sayilar):
        return sum(sayilar)

hesap = HesapMakinesi()
print(hesap.topla(5, 10))         
print(hesap.topla(2, 4, 6, 8, 10)) 

