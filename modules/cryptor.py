from cryptography.fernet import Fernet

# Загрузка содержимого файла .exe в байты
with open('file.exe', 'rb') as f:
    exe_bytes = f.read()

# Генерация ключа для шифрования
key = Fernet.generate_key()
cipher = Fernet(key)

# Шифрование байтов файла .exe
encrypted_exe = cipher.encrypt(exe_bytes)

# Сохранение зашифрованных байтов в файл
with open('crypted_file.exe', 'wb') as f:
    f.write(encrypted_exe)

print("Файл успешно зашифрован.")
print("Ключ для расшифровки:", key)
