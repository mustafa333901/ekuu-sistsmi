def network_configuration():
    print("Ağ Yapılandırması Yapılıyor...")
    network_type = input("Ağ türünü seçin (Wi-Fi / Ethernet): ").lower()
    if network_type == "wi-fi":
        print("Wi-Fi ağı bağlanıyor...")
    elif network_type == "ethernet":
        print("Ethernet kablosu bağlanıyor...")
    else:
        print("Geçersiz ağ türü.")
    
    next_step()

def next_step():
    print("Kuruluma devam etmek için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    network_configuration()
