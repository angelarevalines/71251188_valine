namafile = "alpro.txt"
file = open(namafile).read()

teks = file.lower()

tanda = "!()-[]}{:;.,'?!@#$%^&*_+"
for t in tanda:
    teks = teks.replace(t, "")

kata = teks.split()
unik = set(kata)
print("Kata yang muncul lebih dari 1 kali:")

for k in unik:
    jumlah = kata.count(k)
    if jumlah > 1:
        print(f"{k} = {jumlah} kali")