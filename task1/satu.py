berat = int(input("Berat badan: "))
tinggi = int(input("Tinggi badan: "))

imt = float(berat) / (float(tinggi) * float(tinggi))

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