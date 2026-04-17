kalimat = str(input("Masukkan kalimatmu : "))
kata = kalimat.split()

kata_terpendek = kata[0]
kata_terpanjang = kata[0]

for i in kata:
    if len(i) < len(kata_terpendek):
        kata_terpendek = i
    if len(i) > len(kata_terpanjang):
        kata_terpanjang = i
        
print(f"Kata terpendek = {kata_terpendek} dan kata terpanjang = {kata_terpanjang}")