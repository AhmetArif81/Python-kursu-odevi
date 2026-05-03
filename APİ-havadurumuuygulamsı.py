import requests
import re
sehir = input("Hava durumunu öğrenmek istediğiniz şehri girin: ")

api_key = "b579b2de92cd43018a2172706260305"
url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={sehir}"

cevap = requests.get(url)
ham_veri = cevap.text
derece_eslesme = re.search(r'"temp_c":\s*([0-9.]+)', ham_veri)
durum_eslesme = re.search(r'"text":\s*"([^"]+)"', ham_veri)

if derece_eslesme and durum_eslesme:
    derece = derece_eslesme.group(1)
    durum = durum_eslesme.group(1)
    
    print("\n" + "="*30)
    print(f" {sehir.upper()} GÜNLÜK HAVA RAPORU")
    print("="*30)
    print(f" Sıcaklık : {derece}°C")
    print(f"Hava Durumu : {durum}")
    print("="*30)
else:
    print("Veri çekilemedi. Lütfen şehir adını veya API anahtarınızı kontrol edin.")

