ZayanaCantik = True
ZayaPunyaNopal = True
MerekaPacaran = False

while True:
    if ZayanaCantik and ZayaPunyaNopal:
        print("Zaya dan Nopal pacaran")
        MerekaPacaran = True
        break
    else:
        print("Zaya dan Nopal tidak pacaran")
        MerekaPacaran = False
        break
    
def pacaran():
    if MerekaPacaran:
        print("Zaya dan Nopal pacaran")
    else:
        print("Zaya dan Nopal wajib pacaran")