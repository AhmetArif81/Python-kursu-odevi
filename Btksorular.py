"""
#1.soru   1-100 arasıdaki sayılardan 12ye tam bölünenleri al 
#normla çözüm
onikiyebolunenler=[]
for sayi in range(1,101):
    if (sayi%12==0):
        onikiyebolunenler.append(sayi)
print(onikiyebolunenler)

#list compherean çözümü
onikiyebolunenler2=[sayi for sayi in range(1,101) if (sayi%12==0)]
print(onikiyebolunenler2)

#2.soru  "BTK 2026 egitim yılı 5.donem" metni içindeki rakamları bulup listeleyin isdigit() metodu ile rakam kotrrolu yapabilirsiniz
#normal çözüm
metin="BTK 2026 egitim yılı 5 .dönem"

#list compheresion çözümü
metin="BTK 2026 egitim yılı 5 .dönem"
rakamlar=[char for char in metin if char.isdigit()]
print(rakamlar)

#3.soru  sıcaklık = [10,2,-3,5,0] değerleri 4 derecenin altındaysa buzlanma tehlikesi değilse normal yazın 
#normal çözüm
sicaklik=[10,2,-3,5,0]


#list compherean çözümü 
sicaklik=[10,2,-3,5,0]
sonuc1=["buzlanma tehlikesi var" if i<4 else  "buzlanma yok" for i in sicaklik]
print(sonuc1)

#4.soru 
ogrenciler=["Ali","Ayşe"]
notlar=[40,70]
sonuclar = ["geçti" if n>50  else "kaldı" for n in notlar]
sozluk={ogrenciler:sonuclar for ogrenciler, sonuclar in zip(ogrenciler,sonuclar)}
print(sozluk)


#5.soru 

liste1=[10,20,30]
liste2=[10,20]

carpimlar=[]
for x in liste1:
    for y in liste2: 
        carpimlar.append(x*y)

print(carpimlar)


#öğleden sonra sorular 



#• Veri:
#• ham_veriler = ["Ahmet", " ", "Meryem", None, "Ali", " ", "Selin"]
#• İstenen:
#• 1. None ve sadece boşluktan oluşan verileri filter ile ayıklayın.
#• 2. Kalan isimlerin sağındaki/solundaki boşlukları map ve strip() ile
#  temizleyin.
#• 3. Sonucu temiz_isimler listesi olarak ekrana basın.


ham_veriler = ["Ahmet", " ", "Meryem", None, "Ali", " ", "Selin"]

# 1. Adım: filter ile None ve sadece boşluktan oluşanları ayıklıyoruz.
# lambda x: x and x.strip() ifadesi; x None değilse VE x'in temizlenmiş hali doluysa True döner.
filtreli_veri=filter(lambda x: x is not None and x.strip() !="",ham_veriler)
filtreli_veri = filter(lambda x: x is not None and x.strip() != "", ham_veriler)
# 2. Adım: map ile kalan isimlerin etrafındaki olası boşlukları temizliyoruz.
temiz_isimler_objesi = map(str.strip, filtreli_veri)

# 3. Adım: Sonucu listeye çevirip ekrana basıyoruz.
temiz_isimler = list(temiz_isimler_objesi)

print(f"Temizlenmiş Liste: {temiz_isimler}")

ogrenciler = [
{"ad": "Lale", "notlar": [70, 80, 90]},
{"ad": "Deniz", "notlar": [40, 50, 30]},
{"ad": "Arda", "notlar": [90, 95, 100]},
{"ad": "Zeynep", "notlar": [60, 60, 70]} ]

ogrenciler = [
    {"ad": "Lale", "notlar": [70, 80, 90]},
    {"ad": "Deniz", "notlar": [40, 50, 30]},
    {"ad": "Arda", "notlar": [90, 95, 100]},
    {"ad": "Zeynep", "notlar": [60, 60, 70]}
]

# 1. Adım: map ve lambda ile ortalama ekleme
# update() metodu None döndürdüğü için dict() içinde birleştirme (merge) yöntemi kullanıldı.
ogrenci_ortalamalari = list(map(lambda x: {**x, "ortalama": sum(x["notlar"]) / len(x["notlar"])}, ogrenciler))

# 2. Adım: filter ile başarılı öğrencileri seçme (70 ve üzeri)
basarili_ogrenciler = list(filter(lambda x: x["ortalama"] >= 70, ogrenci_ortalamalari))

# 3. Adım: sorted ile ortalamaya göre büyükten küçüğe sıralama
sirali_liste = sorted(basarili_ogrenciler, key=lambda x: x["ortalama"], reverse=True)

# Sonucu Yazdırma
import json
print(json.dumps(sirali_liste, indent=4, ensure_ascii=False))

"""
