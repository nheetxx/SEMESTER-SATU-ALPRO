matriks = [
    [1, 2, 3],
    [4, 5, 6]
]
print("-" * 10)

print(f"Len matriks = {len(matriks)}")
print(f"Len matriks [i] = {len(matriks[0])}\n")
for i in range(len(matriks)):
    for j in range(len(matriks[i])):
        print(f"Matriks i = {i}, j = {j} ={matriks[i][j]} |", end=" ")
    print()

print("-" * 10)

for baris in matriks:
    for angka in baris:
        print(f"angka={angka}, baris={baris}, {angka * 10} |", end=" ")
    print()

print("-" * 10)


