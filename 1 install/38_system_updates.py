def system_updates():
    print("Sistem güncellemeleri denetleniyor...")
    update_choice = input("Sistem güncellemelerini yüklemek ister misiniz? (Evet / Hayır): ").lower()
    
    if update_choice == "evet":
        print("Sistem güncellemeleri yükleniyor...")
        # Güncelleme işlemleri burada yapılabilir
    else:
        print("Güncellemeler atlandı.")
    
    next_step()

def next_step():
    print("Kuruluma devam etmek için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    system_updates()
