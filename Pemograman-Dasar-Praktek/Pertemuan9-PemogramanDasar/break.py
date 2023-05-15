def main():
    data = [10,20,30,40,50,60,70,80,90,100]
    val = int(input('Masukan nilai yang dicari: '))
    
    index = -1
    for i in range(len(data)) :
        if data[i] == val :
            index = 1
            break
    if index > -1 :
        print(f"{val} ditemukan pada index ke-{i}")
    else :
        print(f"{val} tidak ditemukan")
        
if __name__ == '__main__' :
    main()
    
        