#fungsi cek angka
def cek_angka(a, b, c):
    if (a + b == c) or (a + c == b) or (b + c == a):
        return True
    else:
        return False
    
#testcase
print(cek_angka(2, 2, 4))
print(cek_angka(10, 4, 6))
print(cek_angka(8, 8, 8))
print(cek_angka(2, 3, 4))