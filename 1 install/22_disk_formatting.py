def disk_formatting():
    print("Disk Biçimlendirme Başlıyor...")
    format_choice = input("Tüm verileri silmek istiyor musunuz? (Evet / Hayır): ").lower()
    
    if format_choice == "evet":
        print("Disk biçimlendiriliyor...")
    else:
        print("Disk biçimlendirilmiyor, mevcut veriler korunuyor.")
    
    next_step()

def next_step():
    print("Kuruluma devam etmek için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    disk_formatting()
