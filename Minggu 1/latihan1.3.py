uangerika = 200000000
saldominimal = 400000000
bungapertahun = 10/100
tahunmenabung = 0

#mencari berapa tahun yang dibutuhkan
while uangerika < saldominimal:
    uangerika += uangerika * bungapertahun
    tahunmenabung += 1

print(f"Waktu yang dibutuhkan : {tahunmenabung} tahun")

