#1. soru çözümü
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        baslangic = time.time()
        sonuc = func(*args, **kwargs)
        bitis = time.time
        gecen_sure = bitis - baslangic
        print(f"[{func.__name__}] fonksiyonu {gecen_sure:.4f} saniyede çalıştı.")
        return sonuc 
    return wrapper


@timer_decorator
def test_fonksiyonu(saniye):
    """Belirtilen süre kadar bekleyen örnek bir fonksiyon."""
    time.sleep(saniye)
    return "İşlem Tamamlandı"
test_fonksiyonu(1.5)

#2. soru çözümü 


current_user = {"role": "user"} 

def auth_decorator(gereken_rol):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if current_user.get("role") == gereken_rol:
                return func(*args, **kwargs)
            else:
                return 
        return wrapper
    return decorator


@auth_decorator("admin")
def hassas_verileri_goster():
    return 

@auth_decorator("user")
def profil_bilgilerim():
    return 

# Testler
print(f"Admin İşlemi: {hassas_verileri_goster()}")
print(f"User İşlemi: {profil_bilgilerim()}")