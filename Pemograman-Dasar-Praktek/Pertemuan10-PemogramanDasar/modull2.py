from kartesius import Titik, Garis

def main() :
    a = Titik('A', 0, 0)
    b = Titik('B', 3, 4)
    
    garis = Garis(a, b)
    jarak_A_B = garis.panjang()
    
    print("Jarak titik %s dan %s = %.2f" % (a, b, jarak_A_B))
    
    
if __name__ == '__main__' :
    main()