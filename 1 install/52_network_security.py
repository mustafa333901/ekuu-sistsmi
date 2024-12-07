def network_security():
    print("Ağ güvenliği ayarları yapılıyor...")
    firewall_choice = input("Firewall'u etkinleştirmek ister misiniz? (Evet / Hayır): ").lower()
    
    if firewall_choice == "evet":
        print("Firewall etkinleştirildi.")
    else:
        print("Firewall devre dışı bırakıldı.")
    
    vpn_choice = input("VPN bağlantısını etkinleştirmek ister misiniz? (Evet / Hayır): ").lower()
    
    if vpn_choice == "evet":
        print("VPN bağlantısı etkinleştirildi.")
    else:
        print("VPN bağlantısı devre dışı bırakıldı.")
    
    next_step()

def next_step():
    print("Kuruluma devam etmek için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    network_security()
