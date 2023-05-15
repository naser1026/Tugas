def main() :
    a = int(input("Masukan bilangan bulat: "))

    if a > 0 :
        print(f"{a} adalah bilangan positif")
    
    elif a == 0 :
        print(f"Anda memasukan nilai 0")
    else :
        print(f"{a} adalah bilangan negatif")

if __name__ == '__main__' :
    main()