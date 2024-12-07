def update_drivers():
    print("Sürücü Güncellemeleri Başlıyor...")
    print("Ses, Ekran ve Ağ sürücüleri güncelleniyor...")
    time.sleep(2)  # Simulate driver update process
    print("Sürücü güncellemeleri tamamlandı.")
    next_step()

def next_step():
    print("Kuruluma devam etmek için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    update_drivers()
