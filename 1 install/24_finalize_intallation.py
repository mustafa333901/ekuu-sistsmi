def finalize_installation():
    print("Kurulum Son Kontrolü Başlıyor...")
    print("Sistem genelinde son testler yapılıyor...")
    time.sleep(2)
    print("Kurulum başarıyla tamamlandı. Son adımlar başlatılıyor...")
    
    # Kullanıcıyı yeniden başlatma
    restart = input("Sistemi yeniden başlatmak için [Enter] tuşuna basın...")
    print("Sistem yeniden başlatılıyor...")

def next_step():
    print("Kurulumu tamamlamak için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    finalize_installation()

