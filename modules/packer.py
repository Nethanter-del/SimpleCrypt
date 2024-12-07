# Чтение содержимого файла и запись в переменную
file_path = "file.exe"

with open(file_path, "rb") as file:
    file_content = file.read()

# Создание нового файла и запись в него содержимого
new_file_path = "unpa.exe"

with open(new_file_path, "wb") as new_file:
    new_file.write(file_content)

print("Файл успешно создан с тем же содержимым.")
