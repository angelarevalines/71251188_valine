file1 = input("File pertama : ")
file2 = input("File kedua : ")

try:
    with open(file1) as f1:
        isi_f1 = set(f1.read().lower().split())
    with open(file2) as f2:
        isi_f2 = set(f2.read().lower().split())
    kata_sama = isi_f1 & isi_f2
    
    if len(kata_sama) > 0 :
        urut = sorted(kata_sama)
        hasil = ", ".join(urut)
        print(f"Kata yang sama di kedua file : \n{hasil}")
    else:
        print("Tidak ada kata yang sama")

except FileNotFoundError:
    print("File tidak ditemukan!")