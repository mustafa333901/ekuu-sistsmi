def terminal_settings():
    print("Terminal Ayarları Yapılıyor...")
    terminal_type = input("Terminal türünü seçin (Bash / PowerShell): ").lower()
    
    if terminal_type == "bash":
        print("Bash terminali etkinleştirildi.")
    elif terminal_type == "powershell":
        print("PowerShell terminali etkinleştirildi.")
    else:
        print("Geçersiz seçim, varsayılan terminal kullanılıyor.")
    
    next_step()

def next_step():
    print("Kuruluma devam etmek için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    terminal_settings()
