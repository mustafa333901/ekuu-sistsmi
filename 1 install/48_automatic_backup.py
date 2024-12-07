
İşletim sistemi kurulumunun eksik kısımlarını tamamlayarak, gerekli olan tüm ayarları ve fonksiyonları sağlıyorum. İşte eksik olan ve tamamlanan kısımlar:

46_language_and_region.py – Dil ve Bölge Ayarları
python
Kodu kopyala
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
47_security_and_privacy.py – Güvenlik ve Gizlilik Ayarları
python
Kodu kopyala
def security_and_privacy():
    print("Güvenlik ve gizlilik ayarları yapılıyor...")
    encryption_choice = input("Veri şifrelemesini etkinleştirmek ister misiniz? (Evet / Hayır): ").lower()
    
    if encryption_choice == "evet":
        print("Veri şifreleme etkinleştirildi.")
    else:
        print("Veri şifreleme devre dışı bırakıldı.")
    
    privacy_choice = input("Kişisel bilgilerinizi gizli tutmak ister misiniz? (Evet / Hayır): ").lower()
    
    if privacy_choice == "evet":
        print("Kişisel bilgiler gizli tutulacak.")
    else:
        print("Kişisel bilgiler açık olacak.")
    
    next_step()

def next_step():
    print("Kuruluma devam etmek için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    security_and_privacy()
48_automatic_backup.py
