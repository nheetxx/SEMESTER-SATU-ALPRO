matriksA = [
    [4, 6],
    [8, 9]
]
matriksB = [
    [7, 3],
    [4, 5]
]

print("Matriks A")
for baris in range(len(matriksA)):
    for angka in range(len(matriksA[baris])):
        print(matriksA[baris][angka], end=" ");
    print();

print("\nMatriks B")
for baris in range(len(matriksB)):
    for angka in range(len(matriksB[baris])):
        print(matriksB[baris][angka], end=" ");
    print();

print("\nPenjumlahan Matriks A dan B")
for baris in range(len(matriksA)):
    for angka in range(len(matriksA[baris])):
        print(matriksA[baris][angka] + matriksB[baris][angka], end=" ");
    print();