from cryptography.fernet import Fernet

# Загрузка зашифрованных байтов из файла
with open('crypted_file.exe', 'rb') as f:
    encrypted_exe = f.read()

# Загрузка ключа для расшифровки
key = b'8gw8e0meLuUZDjvD5mj2hMoz67qnlzWYQyahh44VQag='  # Замените 'your_key_here' на ваш ключ

# Инициализация объекта Fernet с использованием ключа
cipher = Fernet(key)

# Расшифровка байтов
decrypted_exe = cipher.decrypt(encrypted_exe)

# Сохранение расшифрованных байтов в новый файл
with open('decrypted_file.exe', 'wb') as f:
    f.write(decrypted_exe)

print("Файл успешно расшифрован.")
