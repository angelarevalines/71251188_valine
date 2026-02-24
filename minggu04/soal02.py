#contoh 4.2
try:
    bilangan = int(input("Masukkan suatu bilangan: "))
    bentukbilangan = "Positif" if bilangan > 0 else "Negatif" if bilangan < 0 else "Nol"
    print(bentukbilangan)

except:
    print("Input tidak valid.")