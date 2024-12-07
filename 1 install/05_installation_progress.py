import time

def installation_progress():
    print("Kurulum Başladı...")
    for i in range(1, 101):
        print(f"Kurulum İlerleme: %{i}")
        time.sleep(0.1)
    
    print("Kurulum tamamlandı. Sistem yeniden başlatılıyor...")
    next_step()

def next_step():
    print("Kurulumu tamamlamak için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    installation_progress()
