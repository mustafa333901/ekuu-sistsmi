def device_customization():
    print("Cihaz Özelleştirmeleri:")
    usage = input("Cihazınızı hangi amaçla kullanacaksınız? (Oyun / İş / Kişisel): ").lower()
    
    if usage == "oyun":
        print("Oyun için optimizasyonlar yapılıyor...")
    elif usage == "iş":
        print("İş amaçlı ayarlamalar yapılıyor...")
    else:
        print("Kişisel kullanım için ayar yapılıyor...")
    
    next_step()

def next_step():
    print("Kuruluma devam etmek için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    device_customization()
