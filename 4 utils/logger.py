# logger.py
def log_error(message):
    print(f"Hata: {message}")
    # Log dosyasına kaydet
    write_log(message)
