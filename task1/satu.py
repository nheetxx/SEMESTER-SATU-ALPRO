berat = float(input("Berat badan: "))
tinggi = float(input("Tinggi badan: "))

tinggi = tinggi / 100   

imt = berat / (tinggi * tinggi)

if imt < 18.5:
    kategori = "Kurus"
elif imt < 25:
    kategori = "Normal"
elif imt < 30:
    kategori = "Gemuk"
else:
    kategori = "Obesitas"

print(f"Berat badan : {berat}")
print(f"Tinggi badan: {tinggi}")
print(f"Kategori    : {kategori}")
print(f"IMT         : {imt}")