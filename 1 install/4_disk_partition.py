def partition_disk():
    print("Disk Bölümleme Seçenekleri")
    print("1. Tüm diskleri biçimlendir")
    print("2. Mevcut bölümleri düzenle")
    choice = input("Seçiminizi yapın (1 / 2): ")
    
    if choice == '1':
        print("Tüm diskler biçimlendiriliyor...")
        next_step()
    elif choice == '2':
        print("Mevcut bölümler düzenleniyor...")
        next_step()
    else:
        print("Geçersiz seçim.")
        partition_disk()

def next_step():
    print("Kuruluma devam etmek için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    partition_disk()
