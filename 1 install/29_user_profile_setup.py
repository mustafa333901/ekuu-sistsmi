def user_profile_setup():
    print("Kullanıcı Profili Ayarları Yapılıyor...")
    full_name = input("Adınızı ve soyadınızı girin: ")
    profile_picture = input("Profil fotoğrafınızı yüklemek ister misiniz? (Evet / Hayır): ").lower()
    
    if profile_picture == "evet":
        print("Profil fotoğrafı yüklendi.")
    
    print(f"Kullanıcı profili başarıyla oluşturuldu: {full_name}")
    next_step()

def next_step():
    print("Kuruluma devam etmek için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    user_profile_setup()
