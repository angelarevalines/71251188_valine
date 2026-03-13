def perkalian(a,b):
    hasil = (a * b)
    proses = ""
    for i in range(1, a + 1):
        proses += str(b)
        if i < a:
            proses += " + "
    print(f"{a} x {b} = {proses} = {hasil}")
    
perkalian(6, 5)
perkalian(7, 10)
