#contoh 4.3
try:
    a = int(input("Masukkan bilangan pertama: "))
    b = int(input("Masukkan bilangan kedua: "))
    c = int(input("Masukkan bilangan ketiga: "))

    if a > b and a > c:
        print ("Bilangan terbesar: ", a)
    elif b > a and b > c:
        print ("Bilangan terbesar ", b)
    else:
        print ("Bilangan terbesar: ", c)

except:
    print ("Input tidak valid")