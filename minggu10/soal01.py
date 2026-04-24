def perbedaan_kata(kalimat1, kalimat2):
    k1 = kalimat1.split()
    k2 = kalimat2.split()

    max_kata = max(len(k1), len(k2))
    beda = 0
    for i in range(max_kata):
        if i < len(k1):
            kata1 = k1[i]
        else:
            kata1 = "tidak ada"

        if i < len(k2):
            kata2 = k2[i]
        else:
            kata2 = "tidak ada"

        if kata1 != kata2:
            beda += 1
    return beda

def perbedaan_file():
    try:
        file1 = input("Masukkan nama file pertama: ")
        file2 = input("Masukkan nama file kedua: ")

        a = open(file1).readlines()
        b = open(file2).readlines()

        max_baris = max(len(a), len(b))

        print("Hasil Perbandingan:\n")

        for i in range(max_baris):
            if i < len(a):
                baris1 = a[i].strip()
            else:
                baris1 = "tidak ada"

            if i < len(b):
                baris2 = b[i].strip()
            else:
                baris2 = "tidak ada"
            
            if baris1 != baris2:
                print(f"Baris ke-{i+1} berbeda:")
                print(f"File 1 : {baris1}")
                print(f"File 2 : {baris2}")
                print(f"Jumlah kata beda : {perbedaan_kata(baris1, baris2)}")
                
    except:
        print("File tidak ditemukan!")

perbedaan_file()