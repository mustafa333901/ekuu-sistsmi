def application_updates():
    print("Uygulama güncellemeleri yapılıyor...")
    app_update_choice = input("Tüm uygulamaları güncellemek ister misiniz? (Evet / Hayır): ").lower()
    
    if app_update_choice == "evet":
        print("Uygulama güncellemeleri yükleniyor...")
        # Uygulama güncellemeleri burada yapılabilir
    else:
        print("Uygulama güncellemeleri atlandı.")
    
    next_step()

def next_step():
    print("Kuruluma devam etmek için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    application_updates()
