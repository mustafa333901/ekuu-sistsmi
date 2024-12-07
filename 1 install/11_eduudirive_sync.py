def eduudrive_sync():
    print("EduuDrive ile Bulut Senkronizasyonu Başlıyor...")
    account = input("EduuDrive hesabınızı bağlamak için e-posta adresinizi girin: ")
    print(f"EduuDrive hesabınız {account} başarıyla bağlandı.")
    next_step()

def next_step():
    print("Kuruluma devam etmek için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    eduudrive_sync()
