def backup_and_restore():
    print("Yedekleme ve geri yükleme ayarları yapılıyor...")
    restore_choice = input("Yedeklerden geri yükleme yapmak ister misiniz? (Evet / Hayır): ").lower()
    
    if restore_choice == "evet":
        print("Yedekleme dosyası geri yükleniyor...")
        # Geri yükleme işlemleri burada yapılabilir
    else:
        print("Yedeklemeler devre dışı bırakıldı.")
    
    next_step()

def next_step():
    print("Kuruluma devam etmek için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    backup_and_restore()
