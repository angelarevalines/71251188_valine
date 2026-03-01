#fungsi untuk mengecek digit bilangan
def cek_digit_belakang(a, b, c):
    if (a % 10 == b % 10) or (a % 10 == c % 10) or (b % 10 == c % 10):
        return True
    else:
        return False

#mengecek test case
print(cek_digit_belakang(30, 20, 18))
print(cek_digit_belakang(145, 25, 100))
print(cek_digit_belakang(71, 187, 18))
print(cek_digit_belakang(1024, 14, 94))
print(cek_digit_belakang(53, 8900, 658))