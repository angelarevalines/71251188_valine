def hitung_kata(a, b):
    a = a.lower()
    b = b.lower()
    
    kalimat_polos = ''
    for i in a:
        if i.isalpha() or i == ' ':
            kalimat_polos += i
    
    pisah = kalimat_polos.split()
    jumlah = pisah.count(b)
    return jumlah

kalimat = str(input("Masukkan kalimatmu : "))   
cari_kata = str(input("Masukkan kata yang dicari : "))

jumlah = hitung_kata(kalimat, cari_kata)
print(f"{cari_kata} ada {jumlah} buah")