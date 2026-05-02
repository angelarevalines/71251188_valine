def tiga_terbaik(data):
    urut = sorted(data, reverse=True)
    bilangan = urut[:3]
    return f"3 bilangan terbaik dari {data} adalah {bilangan}"

print(tiga_terbaik([3,4,8,3,9,40,53,2,6,23]))
print(tiga_terbaik([43,89,9,2,4,7,18,37,22]))