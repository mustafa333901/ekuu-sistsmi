def additional_features():
    print("Ek özellikler kuruluyor...")
    additional_software = input("Ek yazılımlar yüklemek ister misiniz? (Evet / Hayır): ").lower()
    
    if additional_software == "evet":
        print("Ek yazılımlar yükleniyor...")
        # Ek yazılım yükleme işlemleri burada yapılabilir
    else:
        print("Ek yazılımlar yüklenmeyecek.")
    
    next_step()

def next_step():
    print("Kuruluma devam etmek için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    additional_features()
