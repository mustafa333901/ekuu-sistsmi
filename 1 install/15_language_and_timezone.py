def language_and_timezone():
    print("Dil ve Saat Dilimi Seçiliyor...")
    language = input("Dil seçin (English / Türkçe): ").lower()
    timezone = input("Saat dilimi seçin (GMT+0 / GMT+3 / vb.): ").lower()
    
    print(f"Seçilen dil: {language}, Saat dilimi: {timezone}")
    next_step()

def next_step():
    print("Kuruluma devam etmek için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    language_and_timezone()
