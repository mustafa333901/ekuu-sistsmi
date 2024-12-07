def privacy_settings():
    print("Gizlilik Ayarları:")
    location = input("Konum bilgileriniz toplanacak mı? (Evet / Hayır): ").lower()
    ads = input("Hedefli reklamlar için izin veriyor musunuz? (Evet / Hayır): ").lower()
    
    if location == "evet":
        print("Konum bilgileriniz toplanacak.")
    if ads == "evet":
        print("Hedefli reklamlar için izin verildi.")
    
    next_step()

def next_step():
    print("Kuruluma devam etmek için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    privacy_settings()
