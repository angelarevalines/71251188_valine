#masukkan gaji per jam dan jumlah jam kerja selama 1 minggu
gajiperjam = float (input("Berapa gaji per jam Budi? Rp "))
jumlahjamkerja1minggu = float (input("Berapa jam kerja Budi selama 1 minggu? "))
jumlahminggu = 5

#menghitung total gaji selama kerja 5 minggu
totalgaji = round((gajiperjam * jumlahjamkerja1minggu * jumlahminggu),2)

#pendapatan bersih setelah potong pajak
pendapatanbersih = round(totalgaji - (totalgaji * (14/100)),2)

#menghitung uang belanja dan alat tulis
uangbelanja = round(pendapatanbersih * (10/100),2)
uangalattulis = round(pendapatanbersih * (1/100),2)

#menghitung uang setelah belanja 
uangsetelahbelanja = pendapatanbersih - (uangbelanja + uangalattulis)

#menghitung uang yang akan disedekahkan, diterima anak yatim, dan kaum dhuafa
uangsedekah = round(uangsetelahbelanja * (25/100),2)
uanganakyatim = round(uangsedekah * (30/100),2)
uangkaumdhuafa = round((uangsedekah - uanganakyatim),2)

print (f"Pendapatan Budi selama libur musim panas sebelum melakukan pembayaran pajak adalah Rp {totalgaji}")
print (f"Pendapatan Budi selama libur musim panas setelah melakukan pembayaran pajak adalah Rp {pendapatanbersih}")
print (f"Jumlah uang yang Budi habiskan untuk membeli pakaian dan aksesoris adalah Rp {uangbelanja}")
print (f"Jumlah uang yang Budi habiskan untuk membeli alat tulis adalah Rp {uangalattulis}")
print (f"Jumlah uang yang Budi sedekahkan adalah Rp {uangsedekah}")
print (f"Jumlah uang yang akan diterima anak yatim adalah Rp {uanganakyatim}")
print (f"Jumlah uang yang akan diterima kaum dhuafa adalah Rp {uangkaumdhuafa}")

