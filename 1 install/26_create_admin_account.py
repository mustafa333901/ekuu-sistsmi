def create_admin_account():
    print("Yönetici hesabı oluşturuluyor...")
    username = input("Yönetici kullanıcı adı girin: ")
    password = input("Yönetici şifresi oluşturun: ")
    print(f"Yönetici hesabı {username} başarıyla oluşturuldu.")
    next_step()

def next_step():
    print("Kuruluma devam etmek için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    create_admin_account()
