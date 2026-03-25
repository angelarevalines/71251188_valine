def cekangkaprima(angka):
    if angka <= 1:
        return False
    for i in range(2, int(angka**0.5) + 1):
        if angka % i == 0:
            return False
    return True

def angkaprimaterdekat(n):
    for i in range(n - 1, 1, -1):
        if cekangkaprima(i):
            return i

n = int(input("Masukkan bilangan : "))
if n <= 1:
    print("angka tidak valid")
else:
    prima = angkaprimaterdekat(n)
print(f"Bilangan prima terdekat kurang dari {n} adalah {prima}")