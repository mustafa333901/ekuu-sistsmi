def security_and_privacy():
    print("Güvenlik ve gizlilik ayarları yapılıyor...")
    encryption_choice = input("Veri şifrelemesini etkinleştirmek ister misiniz? (Evet / Hayır): ").lower()
    
    if encryption_choice == "evet":
        print("Veri şifreleme etkinleştirildi.")
    else:
        print("Veri şifreleme devre dışı bırakıldı.")
    
    privacy_choice = input("Kişisel bilgilerinizi gizli tutmak ister misiniz? (Evet / Hayır): ").lower()
    
    if privacy_choice == "evet":
        print("Kişisel bilgiler gizli tutulacak.")
    else:
        print("Kişisel bilgiler açık olacak.")
    
    next_step()

def next_step():
    print("Kuruluma devam etmek için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    security_and_privacy()
