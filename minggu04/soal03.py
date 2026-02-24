try:
    bulan = int(input("Masukkan bulan: "))

    if bulan == 2:
        print ("Jumlah hari: 29")
    elif bulan < 8: 
        if bulan % 2 == 1:
            print ("Jumlah hari: 31")
        else:
            print ("Jumlah hari: 30")
    else:
        if bulan % 2 == 1:
            print ("Jumlah hari: 30")
        else:
            print ("Jumlah hari: 31")

except:
    print("Input tidak valid. Tolong masukkan berupa bilangan bulat.")