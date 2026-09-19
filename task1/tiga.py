jenis = input("motor/mobil: ")
jam_masuk = int(input("Jam masuk: "))
menit_masuk = int(input("Menit masuk: "))
jam_keluar = int(input("Jam keluar: "))
menit_keluar = int(input("Menit keluar: "))

durasi_menit = (jam_keluar * 60 + menit_keluar) - (jam_masuk * 60 + menit_masuk)
durasi_jam = durasi_menit // 60

if durasi_menit % 60 != 0:
    durasi_jam += 1
if durasi_jam < 1:
    durasi_jam = 1

if jenis == "motor":
    if durasi_jam == 1:
        biaya = 2000
    else:
        biaya = 2000 + (durasi_jam - 1) * 1000
elif jenis == "mobil":
    if durasi_jam == 1:
        biaya = 5000
    else:
        biaya = 5000 + (durasi_jam - 1) * 2000
else:
    print("Kendaraan apa itu...")
    exit()

print(f"Lama parkir: {durasi_jam} jam")
print(f"Total biaya: Rp{biaya}")