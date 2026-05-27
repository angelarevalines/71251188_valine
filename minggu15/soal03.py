def total(angka):
    if angka < 10:
        return angka
    else:
        return (angka % 10) + total(angka // 10)
    
#TESTCASE
print(total(234))
print(total(12345))
print(total(2523))