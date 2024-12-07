# file_manager.py
def open_file(file_path):
    print(f"{file_path} dosyası açılıyor...")
    # Dosya okuma işlemleri
    with open(file_path, 'r') as file:
        return file.read()
