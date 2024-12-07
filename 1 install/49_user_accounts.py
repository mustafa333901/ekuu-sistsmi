def user_accounts():
    print("Kullanıcı hesapları ayarlanıyor...")
    account_type = input("Hesap türünü seçin (Yönetici / Standart): ").lower()
    
    if account_type == "yönetici":
        print("Yönetici hesabı oluşturuldu.")
    elif account_type == "standart":
        print("Standart kullanıcı hesabı oluşturuldu.")
    else:
        print("Geçersiz seçim, varsayılan hesap türü olarak yönetici seçildi.")
    
    next_step()

def next_step():
    print("Kuruluma devam etmek için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    user_accounts()
