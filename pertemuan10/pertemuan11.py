a = [
    [4, 6],
    [1, 5]
]

b = [
    [7, 3],
    [4, 5]
]

barisA = len(a)
kolomA = len(a[0])
barisB = len(b)
kolomB = len(b[0])

print(f"Baris matriks A: {barisA}\nKolom matriks A: {kolomA}\nBaris matriks B: {barisB}\nKolom matriks B: {kolomB}")

print(f"Matriks A")
for i in a:
    print(i)
    
print(f"Matiks B")
for i in b:
    print(i)
    
print(a[0][0] + b[0][0], a[0][1] + b[0][1])
print(a[1][0] + b[1][0], a[1][1] + b[1][1], "\n")

for i in range(len(a)):
    for j in range(len(a)):
        print(a[i][j] + b[i][j], end=" ")
    print()

for i in range(2):
    for j in range(2):
        print(f"i={[i]} j={[j]}", end=" ")
    print()