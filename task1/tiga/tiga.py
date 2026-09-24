jenis = input("motor/mobil: ")
jamMasuk = int(input("Jam masuk: "))
menitMasuk = int(input("Menit masuk: "))
jamKeluar = int(input("Jam keluar: "))
menitKeluar = int(input("Menit keluar: "))

durasiMenit = (jamKeluar * 60 + menitKeluar) - (jamMasuk * 60 + menitMasuk)
durasiJam = durasiMenit // 60

if durasiMenit % 60 != 0:
    durasiJam += 1
if durasiJam < 1:
    durasiJam = 1

if jenis == "motor":
    if durasiJam == 1:
        biaya = 2000
    else:
        biaya = 2000 + (durasiJam - 1) * 1000
elif jenis == "mobil":
    if durasiJam == 1:
        biaya = 5000
    else:
        biaya = 5000 + (durasiJam - 1) * 2000
else:
    print("Kendaraan apa itu...")
    exit()

print(f"Lama parkir: {durasiJam} jam")
print(f"Total biaya: Rp{biaya}")