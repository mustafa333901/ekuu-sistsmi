# user_manager.py
def add_user(username, password):
    print(f"Kullanıcı {username} ekleniyor...")
    # Kullanıcı bilgilerini veri tabanına kaydet
    save_user_to_db(username, password)
