def jam_email(namaFile):
    try:
        data = open(namaFile)
    except:
        return "File tidak ditemukan."
    hitungJam = {}
    for baris in data:
        if baris.startswith('From '):
            isi = baris.split()
            if len(isi) > 5:
                waktu = isi[5]
                jam = waktu.split(':')[0]
                hitungJam[jam] = hitungJam.get(jam, 0) + 1
    hasil = sorted(hitungJam.items())
    return hasil
for jam, jumlah in jam_email("mbox-short.txt"):
    print(jam, jumlah)