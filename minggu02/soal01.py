#tinggi badan harus dalam meter
tinggibadan = float (input("Tinggi badan (m) = "))

#BMI harus dalam kg/m^2
BMI = float (input("Nilai BMI = "))

#menghitung berat badan
beratbadan = round(BMI * (tinggibadan**2),2)

print (f"Berat badanmu = {beratbadan} kg")