n = int(input("Masukkan jumlah kategori : "))
data_aplikasi = {}

for i in range(n):
    nama_kategori = input(f"Masukkan nama kategori ke-{i+1}: ")
    print(f"Masukkan 5 nama aplikasi di kategori {nama_kategori} : ")
    aplikasi = []
    for j in range(5):
        nama_aplikasi = input(f"Nama aplikasi ke-{j+1}: ")
        aplikasi.append(nama_aplikasi)

    data_aplikasi[nama_kategori] = aplikasi

jumlah_kemunculan = {}
for kategori, daftar_aplikasi in data_aplikasi.items():
    for app in daftar_aplikasi:
        if app in jumlah_kemunculan:
            jumlah_kemunculan[app] += 1
        else:
            jumlah_kemunculan[app] = 1

aplikasi_unik = []
for app, jumlah in jumlah_kemunculan.items():
    if jumlah == 1:
        aplikasi_unik.append(app)

if len(aplikasi_unik) > 0:
    hasil = ', '.join(aplikasi_unik)
    print(f"Aplikasi yang hanya muncul di satu kategori : {hasil}")
else:
    print(f"Aplikasi yang hanya muncul di satu kategori : TIDAK ADA")

if n > 2:
    aplikasi_dua = []
    for app, jumlah in jumlah_kemunculan.items():
        if jumlah == 2:
            aplikasi_dua.append(app)
        
    if len(aplikasi_dua) > 0:
        hasil = ', '.join(aplikasi_dua)
        print(f"Aplikasi yang muncul di dua kategori : {hasil}")
    else:
        print(f"Aplikasi yang muncul di dua kategori : TIDAK ADA")