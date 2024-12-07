def system_health_check():
    print("Sistem sağlık kontrolü yapılıyor...")
    health_choice = input("Sistem sağlık kontrolünü başlatmak ister misiniz? (Evet / Hayır): ").lower()
    
    if health_choice == "evet":
        print("Sistem sağlık kontrolü başlatıldı...")
        # Sağlık kontrolü burada yapılabilir
    else:
        print("Sağlık kontrolü atlandı.")
    
    next_step()

def next_step():
    print("Kuruluma devam etmek için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    system_health_check()
