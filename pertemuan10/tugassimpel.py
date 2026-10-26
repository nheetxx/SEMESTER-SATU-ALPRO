while True:
    barisA = int(input("Jumlah baris matriks A: "))
    kolomA = int(input("Jumlah kolom matriks A: "))
    barisB = int(input("Jumlah baris matriks B: "))
    kolomB = int(input("Jumlah kolom matriks B: "))
    
    matriksA = []
    matriksB = []
    
    for i in range(barisA):
        barisan = []
        for j in range(kolomA):
            angka = int(input(f"Isi Matriks A [Baris {i+1}][Kolom {j+1}]: "))
            barisan.append(angka)
        matriksA.append(barisan)

    for i in range(barisB):
        barisan = []
        for j in range(kolomB):
            angka = int(input(f"Isi Matriks B [Baris {i+1}][Kolom {j+1}]: "))
            barisan.append(angka)
        matriksB.append(barisan)

    print("Hasil Matriks A:")
    for i in matriksA:
        print(i)
    print("Hasil Matriks B:")
    for i in matriksB:
        print(i)
    
    pilihan = input("Pilih opsi\n1. Penjumlahan\n2. Perkalian\n(1/2) ")
    
    if pilihan == "1":
        print("Penjumlahan Matriks A dan B")
        for i in range(len(matriksA)):
            for j in range(len(matriksA[i])):
                print(matriksA[i][j] + matriksB[i][j], end=" ");
            print();

    elif pilihan == "2":
        if kolomA != barisB:
            print(f"{barisA}x{kolomA} dan {barisB}x{kolomB} tidak sesuai syarat.")
            continue
        else:
            hasilPerkalian = []
            for i in range(barisA):
                baris_baru = []
                for j in range(kolomB):
                    baris_baru.append(0)
                hasilPerkalian.append(baris_baru)
            
            for i in range(barisA):
                for j in range(kolomB):
                    for k in range(kolomA):
                        hasilPerkalian[i][j] += matriksA[i][k] * matriksB[k][j]
            
            print("Hasil Perkalian Matriks A dan B:")
            for i in hasilPerkalian:
                print(i)
    else:
        print("Pilihan tidak sesuai")
    break