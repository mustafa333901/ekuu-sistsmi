from datetime import datetime

def time_and_date():
    print("Zaman ve tarih ayarları yapılıyor...")
    current_time = datetime.now()
    print(f"Mevcut tarih ve saat: {current_time}")
    
    set_time = input("Zamanı manuel olarak ayarlamak ister misiniz? (Evet / Hayır): ").lower()
    
    if set_time == "evet":
        time_input = input("Yeni saati girin (HH:MM:SS formatında): ")
        print(f"Saat {time_input} olarak ayarlandı.")
    else:
        print("Otomatik saat alınıyor.")
    
    next_step()

def next_step():
    print("Kuruluma devam etmek için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    time_and_date()
