def show_license_agreement():
    print("EkuuOS Lisans Sözleşmesi")
    print("Bu yazılımı kullanarak, aşağıdaki koşulları kabul etmiş oluyorsunuz...")
    acceptance = input("Lisansı kabul ediyor musunuz? (Evet / Hayır): ").lower()
    if acceptance == "evet":
        print("Lisans kabul edildi, kuruluma devam ediliyor...")
        next_step()
    else:
        print("Kurulum iptal edildi.")
        sys.exit()

def next_step():
    print("Kuruluma devam etmek için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    show_license_agreement()
