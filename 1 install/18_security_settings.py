def security_settings():
    print("Güvenlik Ayarları Yapılıyor...")
    firewall = input("Güvenlik Duvarını açmak istiyor musunuz? (Evet / Hayır): ").lower()
    antivirus = input("Antivirüs programını yüklemek ister misiniz? (Evet / Hayır): ").lower()
    
    if firewall == "evet":
        print("Güvenlik duvarı açıldı.")
    if antivirus == "evet":
        print("Antivirüs programı yüklendi.")
    
    next_step()

def next_step():
    print("Kuruluma devam etmek için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    security_settings()
