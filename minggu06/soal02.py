batas_atas = int(input("Masukkan batas atas = "))
batas_bawah = int(input("Masukkan batas bawah = "))

def ganjil(batas_atas, batas_bawah):
    hasil = []
    
    if batas_bawah < batas_atas:
        for i in range(batas_bawah, batas_atas + 1):
            if i % 2 == 1:
                hasil.append(str(i))
        print(f"bawah = {batas_bawah}, atas = {batas_atas}. Karena bawah<atas, berarti dari kecil ke besar, maka hasilnya adalah:{', '.join(hasil)}.")
    else:
        for i in range(batas_bawah, batas_atas - 1, - 1):
            if i % 2 == 1:
                hasil.append(str(i))
        print(f"bawah = {batas_bawah}, atas = {batas_atas}. Karena bawah>atas, berarti dari besar ke kecil, maka hasilnya adalah:{', '.join(hasil)}.")

ganjil(batas_atas, batas_bawah)
