nama_file = "file03.txt"
print(f"nama file1: {nama_file}")

file = open(nama_file)

for line in file:
    pisah = line.strip().split("||")
    soal = pisah[0].strip()
    jawaban = pisah[1].strip().lower()

    print(soal)
    jawaban_user = input("Jawab: ").lower()

    if jawaban_user == jawaban:
        print("Jawaban benar!\n")
    else:
        print("Jawaban salah!\n")

file.close()