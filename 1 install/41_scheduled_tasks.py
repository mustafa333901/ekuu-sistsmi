def scheduled_tasks():
    print("Zamanlanmış görevler ayarlanıyor...")
    task_choice = input("Zamanlanmış görevleri etkinleştirmek ister misiniz? (Evet / Hayır): ").lower()
    
    if task_choice == "evet":
        print("Zamanlanmış görevler etkinleştirildi.")
        # Görev planlama işlemleri burada yapılabilir
    else:
        print("Zamanlanmış görevler devre dışı bırakıldı.")
    
    next_step()

def next_step():
    print("Kuruluma devam etmek için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    scheduled_tasks()
