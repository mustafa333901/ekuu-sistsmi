def final_configuration():
    print("Son yapılandırmalar yapılıyor...")
    final_settings = input("Son ayarları yapmak ister misiniz? (Evet / Hayır): ").lower()
    
    if final_settings == "evet":
        print("Son yapılandırmalar tamamlandı.")
    else:
        print("Varsayılan ayarlar kullanılıyor.")
    
    next_step()

def next_step():
    print("Kurulumu sonlandırmak için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    final_configuration()
