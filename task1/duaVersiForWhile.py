batas_bawah = int(input("Batas bawah: "))
batas_atas = int(input("Batas atas: "))

if batas_bawah > batas_atas:
    print("Batas bawah tidak boleh lebih besar dari batas atas.")
else:
    bilangan_prima = []
    
    for angka in range(batas_bawah, batas_atas + 1):
        jumlah_pembagi = 0
        
        for pembagi in range(1, angka + 1):
            if angka % pembagi == 0:
                jumlah_pembagi += 1

        if jumlah_pembagi == 2:
            bilangan_prima.append(angka)

    if len(bilangan_prima) == 0:
        print("Tidak ada bilangan prima.")
    else:
        print("Bilangan prima:", *bilangan_prima)

    print("Jumlah bilangan prima:", len(bilangan_prima))