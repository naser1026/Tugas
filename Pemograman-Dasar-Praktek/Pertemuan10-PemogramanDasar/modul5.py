import constant
import writter

def kali(a, b) :
    return a * b

def main() :
    writter.printA()
    writter.printB()
    print('A x B  %d' % kali(constant.A, constant.B))
    
if __name__ == '__main__' :
    main()