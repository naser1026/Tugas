def main() :
    a = int(input("Masukan nomor hari (1 - 7): "))

    if a == 1 :
        print("Senin")
    elif a == 2 :
        print("Selasa")
    elif a == 3 :
        print("Rabu")
    elif a == 4 :
        print("Kamis")
    elif a == 5 :
        print("Jum'at")
    elif a == 6  :
        print("Sabtu")
    elif a == 7 :
        print("Minggu")
    else :
        print("Nilai yang dimasukan salah ")

if __name__ == '__main__' :
    main()