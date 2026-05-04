import sqlite3
import requests
from datetime import datetime
import re

baglanti = sqlite3.connect("btk_final.db")
imlec = baglanti.cursor()

tablo_olusturma_sorgusu = """
CREATE TABLE IF NOT EXISTS kayitlar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    birim_adi TEXT NOT NULL,
    deger REAL NOT NULL,
    islem_tarihi TEXT NOT NULL
)
"""

imlec.execute(tablo_olusturma_sorgusu)
baglanti.commit()

print("Veritabanı ve 'kayitlar' tablosu başarıyla oluşturuldu!")
baglanti.close()


url = "https://api.exchangerate-api.com/v4/latest/USD"

try:
    cevap = requests.get(url, timeout=5)
    cevap.raise_for_status() 
    veri = cevap.json()
    kurlar = veri.get("rates", {})
    

    hedef_kurlar = {
        "EUR": kurlar.get("EUR"),
        "TRY": kurlar.get("TRY")
    }
    
    
    islem_tarihi = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"[{islem_tarihi}] Başarılı! Çekilen Veriler: {hedef_kurlar}")

except requests.exceptions.RequestException as hata:
    print(f"KRİTİK HATA! Veri kaynağına ulaşılamadı. Detay: {hata}")



gelen_json_verisi = {
    "base": "USD",
    "rates": {
        "USD": "1.00 $",      
        "EUR": "0.92 Euro",  
        "GBP": "0.79 GBP",    
        "TRY": "32.45 TL",    
        "JPY": "150.20 ¥"     
    }
}

istenen_kurlar = ["USD", "EUR", "GBP"]
temiz_veriler = {}


for kur, deger in gelen_json_verisi["rates"].items():
    if kur in istenen_kurlar:
        temiz_deger = re.sub(r'[^\d.]', '', str(deger))
        temiz_veriler[kur] = float(temiz_deger)

islem_tarihi = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Temizlenmiş Veriler: {temiz_veriler}\n")


with sqlite3.connect("btk_final.db") as baglanti:
    imlec = baglanti.cursor()
    
    for kur_adi, kur_degeri in temiz_veriler.items():
        sorgu = "INSERT INTO kayitlar (birim_adi, deger, islem_tarihi) VALUES (?, ?, ?)"
        imlec.execute(sorgu, (kur_adi, kur_degeri, islem_tarihi))
    
    baglanti.commit()
    print("Veriler veritabanına başarıyla kaydedildi!\n")


with sqlite3.connect("btk_final.db") as baglanti:
    imlec = baglanti.cursor()
    
    print("--- RAPOR 1: Değeri 0.80'den büyük olanlar ---")
    imlec.execute("SELECT birim_adi, deger FROM kayitlar WHERE deger > 0.80")
    sonuclar_50den_buyuk = imlec.fetchall()
    for satir in sonuclar_50den_buyuk:
        print(f"Kur: {satir[0]}, Değer: {satir[1]}")
        
    print("\n--- RAPOR 2: Her bir kur için kaydedilmiş EN YÜKSEK değerler ---")
    imlec.execute("SELECT birim_adi, MAX(deger) FROM kayitlar GROUP BY birim_adi")
    en_yuksek_degerler = imlec.fetchall()
    for satir in en_yuksek_degerler:
        print(f"Kur: {satir[0]}, Zirve Değer: {satir[1]}")