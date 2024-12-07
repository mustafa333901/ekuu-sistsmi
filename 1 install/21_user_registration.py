def user_registration():
    print("Kullanıcı Kaydı Yapılıyor...")
    username = input("Kullanıcı adı girin: ")
    password = input("Şifre oluşturun: ")
    print(f"Kullanıcı adı {username} olarak kaydedildi.")
    next_step()

def next_step():
    print("Kuruluma devam etmek için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    user_registration()
