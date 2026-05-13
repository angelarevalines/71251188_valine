def identitas_diri(data):
    nama, nim, alamat = data

    print("Data: ", data)
    print()
    print("NIM      :   ", nim)
    print("NAMA     :   ", nama)
    print("ALAMAT   :   ", alamat)
    print()
    print("NIM: ", tuple(nim))
    print()
    print("NAMA DEPAN:  ", tuple(nama.split()[0]))
    print()
    print("NAMA TERBALIK: ", tuple(nama.split()[::-1]))

identitas_diri(('Angela Revaline Setiawan', '71251188', 'Muntilan, Magelang'))