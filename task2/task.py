# silahkan buat perulangan for i untuk looping pertama atau bagian luar, 
# dan for j untuk looping kedua atau bagian dalam, 
# silahkan body loopingnya dibuat sendiri, 
# misal C=i*J atau yang lain, 
# yang penting ada nilai i dan j nya

# i = 1
# for i in range(3):
#     for j in range(1, 5):
#         a = i + j
#         print(a)

# i = 1
# for i in range(3):
#     for j in range(1, 5):
#         a = i + j
#         print("* " * a)

for i in range(3):
    for j in range(2):
        for l in range(2):
            c = i + j + l
            print(f"i = {i}  j = {j}  l = {l}  c = {c}")