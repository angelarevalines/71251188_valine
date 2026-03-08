batas_atas = int(input("Masukkan batas atas = "))
batas_bawah = int(input("Masukkan batas bawah = "))

def ganjil(batas_atas, batas_bawah):
    if batas_bawah < batas_atas:
        for i in range(batas_bawah, batas_atas + 1):
            if i % 2 == 1:
                print(i)
    else:
        for i in range(batas_bawah, batas_atas - 1, - 1):
            if i % 2 == 1:
                print(i)

ganjil(batas_atas, batas_bawah)