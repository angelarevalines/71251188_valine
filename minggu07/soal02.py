def deret(angka):
    for i in range(angka, 0, -1):
        faktorial = 1
        for j in range(1, i + 1):
            faktorial *= j
        
        print(faktorial, end=' ')
        for k in range(i, 0, -1):
            print(k, end=' ')
        print()

angka = int(input("Masukkan nilai n = "))
if angka < 1:
    print("Nilai n harus lebih besar dari 1")
else:
    deret(angka)