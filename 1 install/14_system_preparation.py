def system_preparation():
    print("Sistem Hazırlık Aşaması Başlıyor...")
    print("Dosya sistemi hazırlanıyor, bu işlem birkaç dakika sürebilir.")
    time.sleep(5)
    print("Sistem hazır.")
    next_step()

def next_step():
    print("Kuruluma devam etmek için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    system_preparation()
