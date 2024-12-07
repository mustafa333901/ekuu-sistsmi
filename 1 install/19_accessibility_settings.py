def accessibility_settings():
    print("Erişilebilirlik Ayarları Yapılıyor...")
    high_contrast = input("Yüksek kontrast modunu etkinleştirmek ister misiniz? (Evet / Hayır): ").lower()
    screen_reader = input("Ekran okuyucuyu etkinleştirmek ister misiniz? (Evet / Hayır): ").lower()
    
    if high_contrast == "evet":
        print("Yüksek kontrast modu etkinleştirildi.")
    if screen_reader == "evet":
        print("Ekran okuyucu etkinleştirildi.")
    
    next_step()

def next_step():
    print("Kuruluma devam etmek için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    accessibility_settings()
