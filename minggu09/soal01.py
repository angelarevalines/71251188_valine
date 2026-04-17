def cek_anagram(a, b):
    a = a.strip().lower()
    b = b.strip().lower()

    if len(a) == len(b):
        return sorted(a) == sorted(b)
    return False
    
kata1 = str(input("Masukkan kata pertama = "))
kata2 = str(input("Masukkan kata kedua = "))

if cek_anagram(kata1, kata2):
    print(f"'{kata1}' anagram dengan '{kata2}'")
else:
    print(f"'{kata1}' dan '{kata2}' bukan anagram")
