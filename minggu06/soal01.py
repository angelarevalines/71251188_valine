def perkalian(a, b):
    hasil = (a * b)
    proses = " + ".join([str(b)]* a)
    print(f"{a} x {b} = {proses} = {hasil}")
    
perkalian(6, 5)
perkalian(7, 10)
