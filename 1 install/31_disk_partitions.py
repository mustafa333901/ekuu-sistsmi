def disk_partitions():
    print("Disk bölümlendirme işlemi başlatılıyor...")
    partition_choice = input("Yeni bir bölüm oluşturmak ister misiniz? (Evet / Hayır): ").lower()
    
    if partition_choice == "evet":
        print("Disk bölümleme işlemi başlatıldı...")
        # Bölümleme işlemleri burada yapılabilir
    else:
        print("Disk bölümleme işlemi atlandı.")
    
    next_step()

def next_step():
    print("Kuruluma devam etmek için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    disk_partitions()
