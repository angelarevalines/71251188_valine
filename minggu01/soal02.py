jumlahbeliemas1 = 25
hargaemas1 = 650000

hargabeli1 = jumlahbeliemas1 * hargaemas1

hargaemas2 = 685000
hargasekarang = jumlahbeliemas1 * hargaemas2

keuntungan1 = hargasekarang - hargabeli1
keuntungan1persen = (keuntungan1 / hargabeli1) * 100

print (f"Keuntungan awal Gerard (Rp) : {keuntungan1}")
print (f"Keuntungan awal Gerard (%) : {keuntungan1persen:.2f}%")

jumlahbeliemas2 = 15
totalemassekarang = jumlahbeliemas1 + jumlahbeliemas2
hargaemas3 = 715000

totalhargabeli = (jumlahbeliemas1 * hargaemas1) + (jumlahbeliemas2 * hargaemas2)
totalhargasekarang = totalemassekarang * hargaemas3

keuntungan2 = totalhargasekarang - totalhargabeli
keuntungan2persen = (keuntungan2 / totalhargabeli) * 100

print (f"Keuntungan total Gerard (Rp) : {keuntungan2}")
print (f"Keuntungan total Gerard (%) : {keuntungan2persen:.2f}%")

