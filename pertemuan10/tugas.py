while True:
    barisA = int(input("Jumlah baris matriks A: "))
    kolomA = int(input("Jumlah kolom matriks A: "))
    barisB = int(input("Jumlah baris matriks B: "))
    kolomB = int(input("Jumlah kolom matriks B: "))
    
    matriksA = []
    matriksB = []

    for i in range(barisA):
        baris = []
        for j in range(kolomA):
            angka = int(input(f"Isi matriks A [Baris {i+1}][Kolom {j+1}]: "))
            baris.append(angka)
        matriksA. append(baris)
        
    for i in range(barisB):
        baris = []
        for j in range(kolomB):
            angka = int(input(f"Isi matriks B [Baris {i+1}][Kolom {j+1}]: "))
            baris.append(angka)
        matriksB. append(baris)
        
    print("Hasil matriks A")
    for i in matriksA:
        print(i)
    print("Hasil matriks B")
    for i in matriksB:
        print(i)
        
    pilihan = input("Pilih opsi\n1. Penjumlahan\n2. Perkalian\n(1/2): ")
    
    if pilihan == "1":
        if barisA != barisB or kolomA != kolomB:
            print(f"{barisA}x{kolomA} dan {barisB}x{kolomB} tidak sama.")
            continue
        else:
            print("Hasil penjumlahan matriks A dan matriks B adalah:")
            for i in range(len(matriksA)):
                for j in range(len(matriksA[i])):
                    print(matriksA[i][j] + matriksB[i][j], end=" ")
                print()
    
    elif pilihan == "2":
        if kolomA != barisB:
            print(f"{barisA}x{kolomA} dan {barisB}x{kolomB} tidak memenuhi syarat")
            continue
        else:
            hasilPerkalian = []
            for i in range(barisA):
                barisNew = []
                for j in range(kolomB):
                    barisNew.append(0)
                hasilPerkalian.append(barisNew)
            for i in range(barisA):
                for j in range(kolomB):
                    for k in range(kolomA):
                        hasilPerkalian[i][j] += matriksA[i][k] * matriksB[k][j]
            print("Hasil perkalian matriks A dan matriks B adalah:")
            for i in hasilPerkalian:
                print(i)
                
    else:
        print("Pilihan tidak sesuai.")
        continue
    
    break