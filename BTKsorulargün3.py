# 3.gün öğleden önceki slayt sonu soru çözümleri

# 1. soru çözümü : Öğrenci Durum Takibi
 
class sinif:
    def __init__(self,name,last_name,class_mark):
        self.name=name
        self.last_name=last_name
        self.class_mark=class_mark

    def durum_sorgula(self):
        if self.class_mark > 50 :
            return "Başarılı"
        else:
            return "Başarısız"

ogrenci1=sinif("Ahmet","İpek",45)
ogrenci2=sinif("Mehmet","Selim",90)

print(f"{ogrenci1.name} {ogrenci1.last_name} Durumu: {ogrenci1.durum_sorgula()}")
print(f"{ogrenci2.name} {ogrenci2.last_name} Durumu: {ogrenci2.durum_sorgula()}")


# 2. soru çözümü: Ürün Sayacı

class urunsinifi:

    urunadet=0

    def __init__(self,ad,):
        self.ad=ad
        urunsinifi.urunadet+=1

    @classmethod
    def toplam_urun_sayisini_getir(cls):
        return f"{cls.urunadet} sepete eklendi."
    
print(urunsinifi.toplam_urun_sayisini_getir())

urun1 = urunsinifi("Laptop")
urun2 = urunsinifi("Mouse")
urun3 = urunsinifi("Klavye")
print(urunsinifi.toplam_urun_sayisini_getir())

# 3.soru çözümü: Robot Dünyası 

class Robot:
    toplam_robot_sayisi=0
    def __init__(self,ad,):
        self.ad=ad
        Robot.toplam_robot_sayisi +=1

    def selamla(self):
        print(f"Selamlar ben robotum {self.ad}")

    @classmethod
    def robot_sayisini_sorgula(cls):
        print(f"şuanda dünyada {cls.toplam_robot_sayisi} robot var")
print(Robot.robot_sayisini_sorgula())
r1=Robot("Arifv216")
r2=Robot("Voli")
print(Robot.robot_sayisini_sorgula())


# Öğleden sonraki sorular

class Product:

    def __init__(self,ad,fiyat):
        self.ad=ad
        self.fiyat=fiyat

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self,value):
        if value <0:
            print("fiyat negatif olamaz")
            self.__price=0
        else:
            self.__price=value

    def __eq__(self,other):
        return self.title==other.title

p1=Product("Laptop",80000)
p2=Product("Monitor",45000)


