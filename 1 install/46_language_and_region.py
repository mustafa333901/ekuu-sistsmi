def language_and_region():
    print("Dil ve bölge ayarları yapılıyor...")
    language = input("Dil tercihinizi seçin (Türkçe / İngilizce / Diğer): ").lower()
    
    if language == "türkçe":
        print("Dil olarak Türkçe seçildi.")
    elif language == "ingilizce":
        print("Dil olarak İngilizce seçildi.")
    else:
        print(f"Seçilen dil: {language}.")
    
    region = input("Bölge tercihinizi seçin (TR / US / Diğer): ").lower()
    
    if region == "tr":
        print("Bölge olarak Türkiye seçildi.")
    elif region == "us":
        print("Bölge olarak Amerika Birleşik Devletleri seçildi.")
    else:
        print(f"Seçilen bölge: {region}.")
    
    next_step()

def next_step():
    print("Kuruluma devam etmek için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    language_and_region()
