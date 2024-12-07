def install_security_tools():
    print("Güvenlik araçları kuruluyor...")
    antivirus = input("Antivirüs programı yüklemek ister misiniz? (Evet / Hayır): ").lower()
    firewall = input("Güvenlik duvarını açmak ister misiniz? (Evet / Hayır): ").lower()
    
    if antivirus == "evet":
        print("Antivirüs programı yükleniyor...")
    if firewall == "evet":
        print("Güvenlik duvarı etkinleştiriliyor...")
    
    next_step()

def next_step():
    print("Kuruluma devam etmek için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    install_security_tools()
