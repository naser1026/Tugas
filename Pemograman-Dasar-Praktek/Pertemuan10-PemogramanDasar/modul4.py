import writer
A = 10
B = 20

def kali(a, b) :
    return a * b

def main() :
    writer.printA()
    writer.printB()
    print('A X B= %d' % kali(A, B))
    
if __name__ == '__main__' :
    main()