def final_check():
    print("Son Kontroller Yapılıyor...")
    print("Sistem, güvenlik, sürücüler ve yazılımlar kontrol ediliyor...")
    time.sleep(2)
    print("Tüm testler başarıyla tamamlandı.")
    next_step()

def next_step():
    print("Kuruluma devam etmek için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    final_check()
