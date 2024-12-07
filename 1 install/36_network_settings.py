def network_settings():
    print("Ağ ayarları yapılıyor...")
    ip_address = input("IP adresini manuel olarak girin (otomatik için Enter'a basın): ")
    
    if ip_address:
        print(f"IP adresi {ip_address} olarak ayarlandı.")
    else:
        print("Otomatik IP adresi alındı.")
    
    dns = input("DNS sunucusu adresini girin (otomatik için Enter'a basın): ")
    
    if dns:
        print(f"DNS sunucusu {dns} olarak ayarlandı.")
    else:
        print("Otomatik DNS sunucusu kullanılıyor.")
    
    next_step()

def next_step():
    print("Kuruluma devam etmek için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    network_settings()
