def startup_programs():
    print("Başlangıç programları ayarlanıyor...")
    startup_choice = input("Başlangıçta çalışan programları yönetmek ister misiniz? (Evet / Hayır): ").lower()
    
    if startup_choice == "evet":
        print("Başlangıç programları düzenleniyor...")
        # Başlangıç programları burada ayarlanabilir
    else:
        print("Başlangıç programları varsayılan olarak ayarlanacak.")
    
    next_step()

def next_step():
    print("Kuruluma devam etmek için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    startup_programs()
