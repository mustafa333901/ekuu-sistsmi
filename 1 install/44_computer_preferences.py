def computer_preferences():
    print("Bilgisayar tercihleriniz ayarlanıyor...")
    theme_choice = input("Tema tercihinizi seçin (Koyu / Açık): ").lower()
    
    if theme_choice == "koyu":
        print("Koyu tema seçildi.")
    elif theme_choice == "açık":
        print("Açık tema seçildi.")
    else:
        print("Geçersiz seçim, varsayılan tema kullanılıyor.")
    
    next_step()

def next_step():
    print("Kuruluma devam etmek için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    computer_preferences()
