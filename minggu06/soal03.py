def ips(jumlah_matkul):
    sks = 3
    totalnilai = 0
    bobot = 0
    totalsks = sks * jumlah_matkul
    
    for i in range(jumlah_matkul):
        nilai = str(input(f"Nilai MK {i + 1}: "))
        
        if nilai == "A":
            bobot = 4
        elif nilai == "B":
            bobot = 3
        elif nilai == "C":
            bobot = 2
        elif nilai == "D":
            bobot = 1
        else:
            print("Input tidak valid! Masukkan berupa A/B/C/D")
            return 0
        
        totalnilai = totalnilai + (bobot * sks)
        
    if totalsks == 0:
        return 0
    return totalnilai / totalsks
    
print ("Program penghitung IPS Mahasiswa")
jumlah_matkul = int(input("Berapa jumlah mata kuliah? "))
totalips = ips(jumlah_matkul)
print(f"Nilai IPS anda semester ini {totalips:.2f}")