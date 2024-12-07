import os
import time

def system_reboot():
    print("Sistem yeniden başlatılıyor...")
    time.sleep(2)
    os.system('shutdown /r /t 0')  # Windows sistemlerinde yeniden başlatma komutu

if __name__ == "__main__":
    system_reboot()
