#pengguna perlu menginput bilangan yang akan dicek
a = int(input("Masukkan bilangan pertama = "))
b = int(input("Masukkan bilangan kedua = "))
c = int(input("Masukkan bilangan ketiga = "))

#fungsi untuk mengecek digit bilangan
def cek_digit_belakang(a, b, c):
    if (a % 10 == b % 10) or (a % 10 == c % 10) or (b % 10 == c % 10):
        return True
    else:
        return False

#menampilkan hasil dari inputan pengguna
print(cek_digit_belakang(a, b, c))