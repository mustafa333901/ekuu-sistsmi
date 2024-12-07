def updates_and_patches():
    print("Güncellemeler ve yamalar kontrol ediliyor...")
    patch_choice = input("Güncellemeleri yüklemek ister misiniz? (Evet / Hayır): ").lower()
    
    if patch_choice == "evet":
        print("Güncellemeler ve yamalar yükleniyor...")
        # Güncellemeler burada yapılabilir
    else:
        print("Güncellemeler atlandı.")
    
    next_step()

def next_step():
    print("Kuruluma devam etmek için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    updates_and_patches()
