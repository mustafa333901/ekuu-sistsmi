def log_and_error_handling():
    print("Günlük kaydı ve hata yönetimi başlatılıyor...")
    log_choice = input("Hata günlüklerini etkinleştirmek ister misiniz? (Evet / Hayır): ").lower()
    
    if log_choice == "evet":
        print("Hata günlükleri etkinleştirildi.")
    else:
        print("Hata günlükleri devre dışı bırakıldı.")
    
    next_step()

def next_step():
    print("Kuruluma devam etmek için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    log_and_error_handling()
