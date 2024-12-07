def device_drivers():
    print("Cihaz sürücülerinin kurulumu başlatılıyor...")
    install_drivers = input("Tüm cihaz sürücülerini yüklemek ister misiniz? (Evet / Hayır): ").lower()
    
    if install_drivers == "evet":
        print("Cihaz sürücüleri yükleniyor...")
        # Sürücü yükleme işlemleri burada yapılabilir
    else:
        print("Sürücü yükleme atlandı.")
    
    next_step()

def next_step():
    print("Kuruluma devam etmek için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    device_drivers()
