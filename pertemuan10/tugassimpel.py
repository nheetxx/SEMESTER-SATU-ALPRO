print("Pilih operasi:")
print("1. Penjumlahan")
print("2. Perkalian")
pilihan = input("Pilihan (1/2): ")

barisA = int(input("Jumlah baris matriks A: "))
kolomA = int(input("Jumlah kolom matriks A: "))
barisB = int(input("Jumlah baris matriks B: "))
kolomB = int(input("Jumlah kolom matriks B: "))

if pilihan == "1" and (barisA != barisB or kolomA != kolomB):
    print("Gagal: penjumlahan butuh ukuran matriks yang SAMA.")
elif pilihan == "2" and kolomA != barisB:
    print("Gagal: perkalian butuh kolom A = baris B.")
elif pilihan != "1" and pilihan != "2":
    print("Pilihan tidak sesuai.")

else:
    matriksA = []
    for i in range(barisA):
        baris = []
        for j in range(kolomA):
            angka = int(input(f"A[{i+1}][{j+1}]: "))
            baris.append(angka)
        matriksA.append(baris)

    matriksB = []
    for i in range(barisB):
        baris = []
        for j in range(kolomB):
            angka = int(input(f"B[{i+1}][{j+1}]: "))
            baris.append(angka)
        matriksB.append(baris)

    hasil = []

    if pilihan == "1":
        for i in range(barisA):
            baris = []
            for j in range(kolomA):
                baris.append(matriksA[i][j] + matriksB[i][j])
            hasil.append(baris)

    else:
        for i in range(barisA):
            baris = []
            for j in range(kolomB):
                total = 0
                for k in range(kolomA):
                    total += matriksA[i][k] * matriksB[k][j]
                baris.append(total)
            hasil.append(baris)

    print("Hasil:")
    for baris in hasil:
        print(baris)