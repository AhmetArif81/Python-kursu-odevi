def islem_merkezi(sayi1, sayi2):
    def toplama():
        return sayi1 + sayi2
    
    def cikarma():
        return sayi1 - sayi2
    
    def bolme():
        if sayi2 == 0:
            return "Hata: Sıfıra bölme"
        return sayi1 / sayi2

    sonuclar = {
        "toplam": toplama(),
        "fark": cikarma(),
        "bolum": bolme()
    }
    return sonuclar

sonuc = islem_merkezi(10, 9)
print(sonuc)    


#2. soru 
def logger(seviye):
    # İç fonksiyon: Dışarıdan gelen 'seviye' bilgisini saklar
    def mesaj_yaz(metin):
        # f-string kullanarak formatlı çıktı veriyoruz
        print(f"[{seviye.upper()}] Mesaj: {metin}")
    
    # İç fonksiyonu ÇAĞIRMADAN (parantezsiz) döndürüyoruz
    return mesaj_yaz

# 1. Adım: Farklı görevler için logger'lar oluşturma
bilgi_logla = logger("INFO")
hata_logla = logger("ERROR")

# 2. Adım: Oluşturulan fonksiyonları kullanma
bilgi_logla("Sistem başarıyla başlatıldı.")
hata_logla("Veritabanı bağlantısı başarısız!")


# 3.soru 
import math
def kareal(a):
    return a**2

def kupal(a):
    return a**3

def hesap_makinesi(liste,islem_fonksiyonu):
    sonuc=[]
    for i in liste:
        sonuc.append(islem_fonksiyonu(i))
    return sonuc

sayilar=[1,2,3,4,5,6]
print("kareleri:",hesap_makinesi(kareal,sayilar))
print("kökleri:",hesap_makinesi(kupal,sayilar))
