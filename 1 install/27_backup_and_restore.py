def backup_and_restore():
    print("Yedekleme ve geri yükleme işlemleri başlatılıyor...")
    backup_choice = input("Yedekleme yapmak ister misiniz? (Evet / Hayır): ").lower()
    
    if backup_choice == "evet":
        print("Yedekleme işlemi başlatıldı...")
        # Yedekleme işlemleri burada yapılabilir
    else:
        print("Yedekleme işlemi atlandı.")
    
    restore_choice = input("Geri yükleme işlemi yapmak ister misiniz? (Evet / Hayır): ").lower()
    
    if restore_choice == "evet":
        print("Geri yükleme işlemi başlatıldı...")
        # Geri yükleme işlemleri burada yapılabilir
    else:
        print("Geri yükleme işlemi atlandı.")
    
    next_step()

def next_step():
    print("Kuruluma devam etmek için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    backup_and_restore()
