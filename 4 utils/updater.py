# updater.py
def check_for_updates():
    print("Güncellemeler kontrol ediliyor...")
    # Güncelleme olup olmadığını kontrol et
    update_available = check_for_new_version()
    if update_available:
        apply_update()
