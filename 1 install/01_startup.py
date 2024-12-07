import sys
import time

def show_startup_page():
    print("EkuuOS Kurulum Başlangıcı")
    print("Lütfen dil ve saat dilimini seçin.")
    time.sleep(2)
    language = input("Dil seçin (English / Türkçe): ")
    timezone = input("Saat dilimi seçin: ")
    print(f"Seçilen dil: {language}, Saat dilimi: {timezone}")
    next_step()

def next_step():
    print("Kuruluma başlamak için [Enter] tuşuna basın...")
    input()

if __name__ == "__main__":
    show_startup_page()
