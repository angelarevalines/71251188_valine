import re
import random
import string

kalimat = input("Masukkan kalimatmu = \n")

for i in re.findall(r"\S+@\S+", kalimat):
    username = i.split("@")[0]
    password = ''.join(random.choices(string.ascii_letters + string.digits, k = 8))
    print(f"{i} username: {username}, password: {password}")
    