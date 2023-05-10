import modularitmatika

def main() :
    a = int(input("Masukan nilai a :"))
    b = int(input("Masukan nilai b :"))
    c = float(b)
    
    print("a\t: %d" % a)
    print("b\t: %d" % b)
    print("b\t: %.2f" % c)
    
    print("a - b\t= %d" % modularitmatika.kurang(a, b))
    print("a * b\t= %d" % modularitmatika.kali(a, b))
    print("a // b\t= %d" % modularitmatika.bagi(a, b))
    print("a / c\t= %d" % modularitmatika.bagi(a, b))
    # print("a Mod b\t= %d" % modularitmatika.sisaBagi(a, b))
    print(f"a % b\t= {modularitmatika.sisaBagi(a, b)}")
    print("a ** b\t= %d" % modularitmatika.pangkat(a, b))
    
if __name__ == '__main__' :
    main()