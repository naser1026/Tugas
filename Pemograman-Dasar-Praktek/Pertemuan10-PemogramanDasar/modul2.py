import kartesius

def main() :
    a = kartesius.Titik('A', 0, 0)
    b = kartesius.Titik('B', 3, 4)
    
    garis = kartesius.Garis(a, b)
    jarak_A_B = garis.panjang()
    
    print("Jarak titik %s dan %s = %.2f" % (a, b, jarak_A_B))
    
    
if __name__ == '__main__' :
    main()