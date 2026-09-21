bw = batasBawah = 1
ba = batasAtas = 5

if bw < ba:
    if (bw < 2) or (bw != 2 and bw % 2 == 0) or (bw != 3 and bw % 3 == 0):
        prima = False
    else:
        prima = True
    if prima:
        print(bw)
    bw += 1

    if bw < ba:
        if (bw < 2) or (bw != 2 and bw % 2 == 0) or (bw != 3 and bw % 3 == 0):
            prima = False
        else:
            prima = True
        if prima:
            print(bw)
        bw += 1

        if bw < ba:
            if (bw < 2) or (bw != 2 and bw % 2 == 0) or (bw != 3 and bw % 3 == 0):
                prima = False
            else:
                prima = True
            if prima:
                print(bw)
            bw += 1

            if bw < ba:
                if (bw < 2) or (bw != 2 and bw % 2 == 0) or (bw != 3 and bw % 3 == 0):
                    prima = False
                else:
                    prima = True
                if prima:
                    print(bw)
                bw += 1

                if bw <= ba:
                    if (bw < 2) or (bw != 2 and bw % 2 == 0) or (bw != 3 and bw % 3 == 0):
                        prima = False
                    else:
                        prima = True
                    if prima:
                        print(bw)