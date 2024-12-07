import random


def a1():
    return sum(random.randint(1, 100) for _ in range(random.randint(1, 10)))

def a2():
    try:
        return 10 / 0
    except Exception:
        print()
    # Функция, которая выводит на печать случайный алфавитный символ

def a3():
    print(chr(random.randint(97, 122)))

# Функция, которая просматривает содержимое каталога и выводит случайный файл
def a4():
    import os
    files = os.listdir('.')
    print(random.choice(files))

# Функция, которая создает случайную матрицу 3x3 из случайных чисел и возвращает ее
def a5():
    return [[random.randint(1, 100) for _ in range(3)] for _ in range(3)]

# Функция, которая пытается открыть файл, который не существует
def a6():
    try:
        with open('non_existent_file.txt', 'r') as f:
            print(f.read())
    except Exception:
        print()



# Функция, которая пытается вызвать несуществующий метод объекта
def a8():
    try:
        x = 10
        x.some_nonexistent_method()
    except Exception:
        print()
# Функция, которая случайно сортирует список
def a9():
    my_list = [5, 3, 8, 1, 2]
    random.shuffle(my_list)
    return my_list

# Функция, которая пытается вычислить факториал отрицательного числа
def a10():
    import math
    try:
        return math.factorial(-5)
    except Exception:
        print()
# Функция, которая пытается подключиться к несуществующему хосту
def a11():
    import socket
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('non_existent_host.com', 80))
    except Exception:
        print()

# Функция, которая создает случайный HTTP-запрос
def a12():
    import requests
    try:
        method = random.choice(['GET', 'POST', 'PUT', 'DELETE'])
        url = 'http://example.com'
        response = requests.request(method, url)
        return response.status_code
    except  Exception:
        print


# Функция, которая пытается выполнить SQL-запрос к случайной базе данных
def a15():
    import sqlite3
    try:
        conn = sqlite3.connect('non_existent_database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM non_existent_table")
        rows = cursor.fetchall()
        conn.close()
        return rows
    except Exception:
        print()