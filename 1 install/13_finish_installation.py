def finish_installation():
    print("Kurulum Tamamlanıyor...")
    print("EkuuOS kurulumunun tamamlanması için sistem yeniden başlatılıyor...")
    time.sleep(3)
    print("Sistem yeniden başlatılıyor...")
    next_step()

def next_step():
    print("Kurulumu tamamlamak için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    finish_installation()
