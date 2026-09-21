batasBawah = 1 
batasAtas = 5

if batasBawah < batasAtas:
    print(batasBawah) #print 1
    batasBawah += 1 # batas bawahnya jadi 2
    if batasBawah < batasAtas:
        print(batasBawah) #print 2
        batasBawah += 1 # batas bawahnya jadi 3
        if batasBawah < batasAtas:
            print(batasBawah) #print 3
            batasBawah += 1 # batas bawahnya jadi 4
            if batasBawah < batasAtas:
                print(batasBawah) #print 4
                batasBawah += 1 # batas bawah jadi 5
                if batasBawah <= batasAtas:
                    print(batasBawah) #print 5
    
    