import re
from datetime import datetime

kalimat = input("Masukkan kalimatmu : ")

daftar_tanggal = re.findall(r"\d{4}-\d{2}-\d{2}", kalimat)
hari_ini = datetime.now()

for tgl in daftar_tanggal:
    tgl_obj = datetime.strptime(tgl, "%Y-%m-%d")
    selisih = (hari_ini- tgl_obj).days
    
    print(f"{tgl_obj} selisih {selisih} hari")
    