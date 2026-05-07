try:
    hitung_domain = {}
    filename = input("Masukkan nama file : ")
    file = open(filename)
    
    for line in file:
        if line.startswith("From "):
            isi = line.split()
            if len(isi) > 1:
                email = isi[1]
                domain = email.split("@")[-1]
                hitung_domain[domain] = hitung_domain.get(domain, 0) + 1
    print(hitung_domain)
    file.close()
except FileNotFoundError:
    print("File tidak ditemukan!")