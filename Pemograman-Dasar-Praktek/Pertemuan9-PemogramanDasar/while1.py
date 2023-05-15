def main() :
    total = 0
    i = 1
    while i <= 5 :
        print(i, end= "")
        print(" + " if i < 5 else " = ", end="")
        total += i
        i += 1
    print(total)
    
if __name__ == '__main__' :
    main()