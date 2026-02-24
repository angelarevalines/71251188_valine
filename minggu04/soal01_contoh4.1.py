#contoh4.1
try:
    suhu = float(input("Masukkan suhu tubuh (celcius): "))
    if suhu >= 38:
        print("Anda demam")
    else:
        print("Anda tidak demam")

except:
    print("Tolong masukkan suhu berupa angka.")