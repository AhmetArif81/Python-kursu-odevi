import abc

# 1. TEMEL SINIFLANDIRMA 
class BaseProduct(abc.ABC):
    def __init__(self, stock_code, price, weight, stock_quantity):
        self.stock_code = stock_code
        self.price = price
        self.weight = weight
        self._stock_quantity = stock_quantity

    @property
    def stock_code(self):
        return self._stock_code

    @stock_code.setter
    def stock_code(self, value):
        if len(value) < 3:
            raise ValueError("Stok kodu en az 3 karakter olmalıdır")
        self._stock_code = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Fiyat negatif olamaz.")
        self._price = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value < 0:
            raise ValueError("Ağırlık negatif olamaz")
        self._weight = value

    @abc.abstractmethod
    def calculate_shipping(self):
        pass

    def __str__(self):
        return f"Kod: {self._stock_code} | Fiyat: {self._price} | Stok: {self._stock_quantity}"


#2 ALT SINIFLAR 
class ElectronicProduct(BaseProduct):
    def __init__(self, stock_code, price, weight, stock_quantity, warranty_period):
        super().__init__(stock_code, price, weight, stock_quantity)
        self.warranty_period = warranty_period

    def calculate_shipping(self):
        return 50 + (self.weight * 2)

class FoodProduct(BaseProduct):
    def __init__(self, stock_code, price, weight, stock_quantity, expiry_date):
        super().__init__(stock_code, price, weight, stock_quantity)
        self.expiry_date = expiry_date

    def calculate_shipping(self):
        return 30 + (self.weight * 1.5)

class HazardousProduct(BaseProduct):
    def __init__(self, stock_code, price, weight, stock_quantity, safety_level):
        super().__init__(stock_code, price, weight, stock_quantity)
        self.safety_level = safety_level

    def calculate_shipping(self):
        return 200 + (self.weight * 10)


# 3. YÖNETİM VE İŞLEM SINIFLARI
class InventoryManager:
    def __init__(self):
        self.products = []
        self._index = 0

    def add_product(self, product):
        self.products.append(product)

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self.products):
            result = self.products[self._index]
            self._index += 1
            return result
        raise StopIteration

class LogisticsProcessor:
    @staticmethod
    def calculate_total_shipping(product):
        return product.calculate_shipping()

    @staticmethod
    def get_critical_stocks(inventory_manager, limit=10):
        for product in inventory_manager:
            if product._stock_quantity < limit:
                yield product


# 4 KONSOL UYGULAMASI 
def main():
    manager = InventoryManager()
    processor = LogisticsProcessor()

    while True:
        print("\n--- Akıllı Depo Sistemi ---")
        print("1. Ürün Ekle\n2. Listele\n3. Kritik Stok Kontrolü\n4. Çıkış")
        choice = input("Seçiminiz: ")

        try:
            if choice == "1":
                t = input("Tür (E:Elektronik, G:Gıda, T:Tehlikeli): ").upper()
                kod = input("Stok Kodu: ")
                fiyat = float(input("Fiyat: "))
                agirlik = float(input("Ağırlık: "))
                stok = int(input("Stok Miktarı: "))

                if t == "E":
                    garanti = int(input("Garanti Süresi (Ay): "))
                    p = ElectronicProduct(kod, fiyat, agirlik, stok, garanti)
                elif t == "G":
                    tarih = input("Son Tüketim (YYYY-AA-GG): ")
                    p = FoodProduct(kod, fiyat, agirlik, stok, tarih)
                elif t == "T":
                    seviye = input("Tehlike Seviyesi: ")
                    p = HazardousProduct(kod, fiyat, agirlik, stok, seviye)
                else:
                    print("Hatalı tür seçimi!")
                    continue
                
                manager.add_product(p)
                print("Ürün başarıyla eklendi.")

            elif choice == "2":
                print("\n--- Tüm Ürünler ---")
                for p in manager:
                    maliyet = processor.calculate_total_shipping(p)
                    print(f"{p} | Kargo Maliyeti: {maliyet} TL")

            elif choice == "3":
                print("\n--- Kritik Stok Uyarısı ---")
                for p in processor.get_critical_stocks(manager):
                    print(f"UYARI: {p.stock_code} kodlu üründen {p._stock_quantity} adet kaldı!")

            elif choice == "4":
                print("Sistemden çıkılıyor...")
                break
        
        except ValueError as e:
            print(f"Hata: {e}. Lütfen girişlerinizi kontrol edin.")

if __name__ == "__main__":
    main()