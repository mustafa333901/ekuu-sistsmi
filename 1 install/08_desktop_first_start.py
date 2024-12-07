def desktop_first_start():
    print("Masaüstü Özelleştiriliyor...")
    theme = input("Hangi temayı seçmek istersiniz? (Koyu / Açık): ").lower()
    if theme == "koyu":
        print("Koyu tema seçildi.")
    elif theme == "açık":
        print("Açık tema seçildi.")
    else:
        print("Geçersiz seçim.")
    
    next_step()

def next_step():
    print("Kuruluma devam etmek için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    desktop_first_start()
