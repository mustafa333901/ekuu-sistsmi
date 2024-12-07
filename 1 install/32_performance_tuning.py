def performance_tuning():
    print("Performans Ayarları Yapılıyor...")
    performance_mode = input("Performans modunu seçin (Düşük / Orta / Yüksek): ").lower()
    
    if performance_mode == "düşük":
        print("Düşük performans modu seçildi.")
    elif performance_mode == "orta":
        print("Orta performans modu seçildi.")
    elif performance_mode == "yüksek":
        print("Yüksek performans modu seçildi.")
    else:
        print("Geçersiz seçim, varsayılan performans moduna geçildi.")
    
    next_step()

def next_step():
    print("Kuruluma devam etmek için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    performance_tuning()
