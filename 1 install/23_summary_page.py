def summary_page():
    print("Kurulum Özeti:")
    print("1. Sistem hazırlığı tamamlandı.")
    print("2. Sürücüler güncellendi.")
    print("3. Güvenlik ayarları yapıldı.")
    print("4. Sistem yeniden başlatıldı.")
    
    print("Kurulum başarıyla tamamlandı!")
    next_step()

def next_step():
    print("Kurulumu sonlandırmak için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    summary_page()
