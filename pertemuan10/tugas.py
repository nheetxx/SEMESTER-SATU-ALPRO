bA = [[]]
kA = [[]]
bB = [[]]
kB = [[]]
while True:
    barisA = int(input("Masukkan jumlah baris matriks A"))
    kolomA = int(input("Masukkan jumlah kolom matriks A"))
    barisB = int(input("Masukkan jumlah baris matriks B"))
    kolomB = int(input("Masukkan jumlah kolom matriks B"))

    bA = [0] * barisA
    kA = [0] * kolomA
    bB = [0] * barisB
    kB = [0] * kolomB

    for i in range(barisA):
        isiBarisA = int(input(f"Masukkan isi baris ke-{i+1} A"))
        bA[i] = isiBarisA
        
    for i in range(kolomA):
        isiKolomA = int(input(f"Masukkan isi kolom ke-{i+1} A"))
        kA[i] = isiKolomA
        
    for i in range(barisB):
        isiBarisB = int(input(f"Masukkan isi baris ke-{i+1} B"))
        bB[i] = isiBarisB
        
    for i in range(kolomB):
        isiKolomB = int(input(f"Masukkan isi kolom ke-{i+1} A"))
        kA[i] = isiKolomA
    break

print(bA)
print(kA)
print(bB)
print(kA)
    
# for i in range(len(hasil)):
#     for j in range(len(hasil[i])):
#         print(f"Matriks i = {i}, j = {j} ={hasil[i][j]} |", end=" ")
#     print()