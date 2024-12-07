def apps_and_features():
    print("Uygulamalar ve Özellikler Seçiliyor...")
    apps = ["Fotoğraflar", "Medya Oynatıcı", "Paint", "Eduu Edge"]
    print("Yüklemek istediğiniz uygulamaları seçin:")
    for i, app in enumerate(apps, 1):
        print(f"{i}. {app}")
    
    selection = input("Seçiminizi yapın (1-4): ")
    print(f"Seçilen uygulama: {apps[int(selection) - 1]}")
    next_step()

def next_step():
    print("Kuruluma devam etmek için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    apps_and_features()
