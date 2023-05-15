print("=======================================================")
print("Program Break dan Continue")
print("=======================================================")

j = 1
while j < 11 :
    if j == 4 :
        print(" 4 tidak ditemukan karena semua baris dilewati")
    if j > 8 :
        print(" j lebih besar dari 8, maka program keluar dari while")
        break
    print(j)
    j += 1