def average():
    hasil = []
    print('Masukkan bilangan-bilangan dan ketik "done" jika sudah selesai')
    
    while True: 
        angka = input("Bilangan = ")
        if angka.lower() == "done":
            break
        try: 
            bilangan = float(angka)
            hasil.append(bilangan)
        except:
            print("Masukkan angka yang valid!")

    if len(hasil) > 0:
        ratarata = sum(hasil) / len(hasil)
        print(f"rata-rata dari {len(hasil)} bilangan yang dimasukkan adalah {ratarata:.2f}")
    else:
        print("Tidak ada bilangan yang kamu masukkan")

average()