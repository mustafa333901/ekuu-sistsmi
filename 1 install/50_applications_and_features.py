def applications_and_features():
    print("Uygulamalar ve özellikler ayarlanıyor...")
    app_choice = input("Varsayılan uygulamaları yüklemek ister misiniz? (Evet / Hayır): ").lower()
    
    if app_choice == "evet":
        print("Varsayılan uygulamalar yükleniyor...")
        # Uygulama yükleme işlemleri burada yapılabilir
    else:
        print("Varsayılan uygulamalar yüklenmeyecek.")
    
    next_step()

def next_step():
    print("Kuruluma devam etmek için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    applications_and_features()
