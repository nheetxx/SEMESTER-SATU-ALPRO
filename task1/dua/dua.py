from sympy import primerange

batas_bawah = int(input("Masukkan batas bawah: "))
batas_atas = int(input("Masukkan batas atas: "))


if batas_bawah > batas_atas:
    print("Batas bawah tidak boleh lebih besar dari batas atas.")
    exit()
else:
    bilangan_prima = list(primerange(batas_bawah, batas_atas + 1))

print("Bilangan prima:", *bilangan_prima)
print("Jumlah bilangan prima:", len(bilangan_prima))