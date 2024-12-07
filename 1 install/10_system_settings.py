def system_settings():
    print("Sistem Ayarları Yapılıyor...")
    power_plan = input("Güç planı seçin (Verimli / Yüksek Performans): ").lower()
    
    if power_plan == "verimli":
        print("Verimli güç planı seçildi.")
    elif power_plan == "yüksek performans":
        print("Yüksek performans gücü seçildi.")
    else:
        print("Geçersiz seçim, varsayılan ayarlar kullanılıyor.")
    
    next_step()

def next_step():
    print("Kuruluma devam etmek için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    system_settings()
