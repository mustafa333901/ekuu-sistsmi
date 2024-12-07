def choose_installation_type():
    print("Kurulum Türünü Seçin:")
    print("1. Yükseltme (Upgrade)")
    print("2. Temiz Kurulum (Custom)")
    choice = input("Seçiminizi yapın (1 / 2): ")
    
    if choice == '1':
        print("Yükseltme seçildi. Mevcut sistemi yükseltiyoruz...")
        next_step()
    elif choice == '2':
        print("Temiz kurulum seçildi. Tüm veriler silinecek!")
        next_step()
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
        choose_installation_type()

def next_step():
    print("Kuruluma devam etmek için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    choose_installation_type()
