try:
    hitung_email = {}
    filename = input("Masukkan nama file : ")
    file = open(filename)

    for line in file:
        if line.startswith("From "):
            isi = line.split()
            if len(isi) > 1:
                email = isi[1]
                hitung_email[email] = hitung_email.get(email, 0) + 1
    print(hitung_email)
    file.close()
except FileNotFoundError:
    print("File tidak ditemukan!")